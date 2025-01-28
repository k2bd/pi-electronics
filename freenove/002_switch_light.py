from gpiozero import LED, Button

def main():
    led = LED(17)
    button = Button(18)

    while True:
        if button.is_pressed:
            led.on()
        else:
            led.off()



if __name__ == "__main__":
    main()
