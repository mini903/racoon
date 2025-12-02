import pigpio
import time

# -----------------------------
# pigpio 초기화
# -----------------------------
pi = pigpio.pi()
if not pi.connected:
    print("pigpio 데몬이 실행 중인지 확인하세요!")
    exit()

# -----------------------------
# GPIO 핀 설정
# -----------------------------
PWM_LEFT = 17
DIR_LEFT = 27
PWM_RIGHT = 18
DIR_RIGHT = 22

PWM_LIFT = 23
DIR_LIFT = 24

# GPIO 출력 설정
pi.set_mode(PWM_LEFT, pigpio.OUTPUT)
pi.set_mode(DIR_LEFT, pigpio.OUTPUT)
pi.set_mode(PWM_RIGHT, pigpio.OUTPUT)
pi.set_mode(DIR_RIGHT, pigpio.OUTPUT)
pi.set_mode(PWM_LIFT, pigpio.OUTPUT)
pi.set_mode(DIR_LIFT, pigpio.OUTPUT)

# PWM 주파수 설정 (1kHz)
pi.set_PWM_frequency(PWM_LEFT, 1000)
pi.set_PWM_frequency(PWM_RIGHT, 1000)
pi.set_PWM_frequency(PWM_LIFT, 1000)

# -----------------------------
# 주행 모터 함수
# -----------------------------
def drive(left_speed, right_speed, left_dir=True, right_dir=True):
    pi.write(DIR_LEFT, 1 if left_dir else 0)
    pi.write(DIR_RIGHT, 1 if right_dir else 0)

    # PWM duty 0~255 변환 (0~100은 %로 사용하던 것 그대로 유지)
    pi.set_PWM_dutycycle(PWM_LEFT, int(left_speed * 2.55))
    pi.set_PWM_dutycycle(PWM_RIGHT, int(right_speed * 2.55))

# -----------------------------
# 리프트 모터 함수
# -----------------------------
def lift(speed, direction=True):
    pi.write(DIR_LIFT, 1 if direction else 0)
    pi.set_PWM_dutycycle(PWM_LIFT, int(speed * 2.55))

# -----------------------------
# 테스트 동작
# -----------------------------
try:
    # 주행: 전진
    drive(left_speed=80, right_speed=80, left_dir=True, right_dir=True)

    # 리프트 올리기
    lift(speed=70, direction=True)
    time.sleep(3)

    # 주행: 후진
    drive(left_speed=50, right_speed=50, left_dir=False, right_dir=False)

    # 리프트 내리기
    lift(speed=50, direction=False)
    time.sleep(3)

    # 정지
    drive(0, 0)
    lift(0)

finally:
    pi.stop()
