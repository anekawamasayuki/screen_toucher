import RPi.GPIO as GPIO
import time
import random

PNO = 14 # 抵抗に繋いだ側の、GPIOポート番号
TOGGLE = 2

GPIO.cleanup() # reset

GPIO.setmode(GPIO.BCM)
GPIO.setup(PNO, GPIO.OUT)
GPIO.setup(TOGGLE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    try:
        if not GPIO.input(TOGGLE):
            GPIO.output(PNO, GPIO.HIGH) # 点灯
            sleep_seconds = 0.1 + 0.133 * random.random()
            print("ON: {}".format(sleep_seconds))
            time.sleep(sleep_seconds)
            GPIO.output(PNO, GPIO.LOW) # 消灯
            sleep_seconds = 0.1 + 0.133 * random.random()
            print("OFF: {}".format(sleep_seconds))
            time.sleep(sleep_seconds)
        else:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ctrl+Cで停止しました")
        break

GPIO.cleanup()
