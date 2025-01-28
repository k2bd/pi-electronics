from gpiozero import LED, Button
from signal import pause

def main():
    led = LED(17)
    button = Button(18)

    button.when_activated(led.toggle)

    pause()



if __name__ == "__main__":
    main()
