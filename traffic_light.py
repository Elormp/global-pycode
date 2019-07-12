from gpiozero import LED, Button
from time import sleep
from signal import pause




led = LED(18)
led1 = LED(22)
led2 = LED(27)
button = Button(2)





while True:
    
    button.when_pressed = led.on
    button.when_released = led.off
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.1)
    
    led1.on() 
    button.when_pressed = led1.on
    sleep(0.5)
    
    led1.off()
    button.when_released = led1.off
    sleep(0)
    
    
    button.when_pressed = led2.on
    button.when_released = led2.off
    led2.on()
    sleep(0.5)
    led2.off()
    sleep(0)
    
pause()