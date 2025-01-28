from gpiozero import LED
import time


def main():
    led = LED(17)

    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)


if __name__ == "__main__":
    main()
