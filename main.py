import asyncio
import json
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.websockets import WebSocketDisconnect
from control import drive, stop, set_logger

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_index():
    return FileResponse("static/index.html")

@app.websocket("/ws/joystick")
async def joystick_endpoint(websocket: WebSocket):
    await websocket.accept()

    def send_log(msg: str):
        async def _safe_send():
            try:
                await websocket.send_text(msg)
            except Exception:
                pass
        asyncio.create_task(_safe_send())

    set_logger(send_log)

    await websocket.send_text("사용자 연결됨")

    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            x = float(payload.get("x", 0))
            y = float(payload.get("y", 0))
            drive(x, y)
    except WebSocketDisconnect:
        stop()
        print("사용자 연결 종료")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
