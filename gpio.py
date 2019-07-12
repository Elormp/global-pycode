'''from gpiozero import LED
import time

led = LED(18)

led.on()
time.sleep(5)
led.off()'''



'''from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)'''

'''from gpiozero import LED, Button
from signal import pause

led = LED(18)
button = Button(2)
led.on()
button.when_pressed = led.off
button.when_released = led.on

pause()'''

from gpiozero import LED, Button
from signal import pause

led = LED(18)
button = Button(2)
button.when_pressed = led.on
button.when_released = led.off

pause()




'''from subprocess import call

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing'''