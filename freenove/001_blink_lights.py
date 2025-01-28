from gpiozero import LED
import time


def main(delay: float = 1.0):
    led = LED(17)

    while True:
        led.on()
        time.sleep(delay)
        led.off()
        time.sleep(delay)


if __name__ == "__main__":
    main(delay=0.5)
