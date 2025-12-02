import RPi.GPIO as GPIO
import time

# -----------------------------
# GPIO 설정
# -----------------------------
GPIO.setmode(GPIO.BCM)

# 주행 좌/우
PWM_LEFT = 17
DIR_LEFT = 27
PWM_RIGHT = 18
DIR_RIGHT = 22

# 리프트
PWM_LIFT = 23
DIR_LIFT = 24

GPIO.setup(PWM_LEFT, GPIO.OUT)
GPIO.setup(DIR_LEFT, GPIO.OUT)
GPIO.setup(PWM_RIGHT, GPIO.OUT)
GPIO.setup(DIR_RIGHT, GPIO.OUT)
GPIO.setup(PWM_LIFT, GPIO.OUT)
GPIO.setup(DIR_LIFT, GPIO.OUT)

# PWM 초기화 (1kHz)
pwm_left = GPIO.PWM(PWM_LEFT, 1000)
pwm_right = GPIO.PWM(PWM_RIGHT, 1000)
pwm_lift = GPIO.PWM(PWM_LIFT, 1000)

pwm_left.start(0)
pwm_right.start(0)
pwm_lift.start(0)

# -----------------------------
# 주행 모터 함수
# -----------------------------
def drive(left_speed, right_speed, left_dir=True, right_dir=True):
    GPIO.output(DIR_LEFT, GPIO.HIGH if left_dir else GPIO.LOW)
    GPIO.output(DIR_RIGHT, GPIO.HIGH if right_dir else GPIO.LOW)
    pwm_left.ChangeDutyCycle(left_speed)
    pwm_right.ChangeDutyCycle(right_speed)

# -----------------------------
# 리프트 모터 함수
# -----------------------------
def lift(speed, direction=True):
    GPIO.output(DIR_LIFT, GPIO.HIGH if direction else GPIO.LOW)
    pwm_lift.ChangeDutyCycle(speed)

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

    # 모터 정지
    drive(0, 0)
    lift(0)

finally:
    pwm_left.stop()
    pwm_right.stop()
    pwm_lift.stop()
    GPIO.cleanup()
