from gpiozero import PWMLED
import time
import math

def main(
    *,
    period_seconds: float = 2.0,
    update_interval_seconds: float = 1 / 30,
    min_brightness: float = 0.0,
    max_brightness: float = 1.0
):
    if max_brightness < min_brightness:
        raise ValueError("min_brightness must be less than max_brightness")
    led = PWMLED(18, initial_value=0, frequency=1000)

    start = time.time()

    while True:
        duration = start - time.time()

        # Brightness on range [0, 1]
        brightness = (1 + math.sin(duration * 2 * math.pi / period_seconds)) / 2

        # Brightness on range [min, max]
        brightness = brightness * (max_brightness-min_brightness) + min_brightness

        # print(brightness)
        led.value = brightness

        time.sleep(update_interval_seconds)


if __name__ == "__main__":
    main(period_seconds=3.5, min_brightness=0.1, max_brightness=0.9)
