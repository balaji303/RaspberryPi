from gpiozero import PWMLED
from time import sleep

led=PWMLED(21)

while True:
      led.value=0
      sleep(1)
      led.value=0.25 
      sleep(1)
      led.value=0.5
      sleep(1)
      led.value=0.75
      sleep(1)
      led.value=1
      sleep(1)