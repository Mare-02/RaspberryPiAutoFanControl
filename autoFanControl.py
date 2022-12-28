import subprocess
import time
import RPi.GPIO as GPIO

SLEEP_INTERVAL = 10  # (seconds) How often we check the core temperature.
GPIO_PIN = 18  # Which GPIO pin you're using to control the fan.


def get_temp():
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        return 50   # if the function didnt work, just return 50
    
if __name__ == '__main__':
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)

    speed = 0
    minSpeed = 30
    maxSpeed = 100

    p = GPIO.PWM(GPIO_PIN, 50)  # frequency=50Hz
    p.start(0)

    while True:
        temp = get_temp()

        if temp > 60:
            speed = maxSpeed
        elif temp > 50:
            speed = 80
        elif temp > 40:
            speed = 60
        elif temp > 30:
            speed = 40
        else:
            speed = minSpeed

        p.ChangeDutyCycle(speed)

        time.sleep(SLEEP_INTERVAL)

    GPIO.cleanup()

