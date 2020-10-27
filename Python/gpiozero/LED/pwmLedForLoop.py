from gpiozero import PWMLED
from time import sleep
a=0.0
led=PWMLED(21)
while True:
    if a<1:
      led.value=a
      a=a+0.1
    else:
      a=0
    sleep(1)
