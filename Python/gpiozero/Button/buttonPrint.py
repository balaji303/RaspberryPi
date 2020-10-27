from gpiozero import Button
from signal import pause
button=Button(20)

def pressed():
    print("***ON***")

def relesed():
    print("OFF")
    
button.when_pressed= pressed
button.when_released= relesed

pause()
