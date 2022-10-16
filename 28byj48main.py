from machine import Pin
from time import sleep
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

IN1 = Pin(2,Pin.OUT)
IN2 = Pin(3,Pin.OUT)
IN3 = Pin(4,Pin.OUT)
IN4 = Pin(5,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

display.set_backlight(0.5)
display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)

def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
    
def motion(suunta, speed):
    global pins
    if suunta == 1:
        pins = [IN4, IN3, IN2, IN1]
    else:
        pins = [IN1, IN2, IN3, IN4]
    for step in sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(speed)

clear()

while True:
    if button_a.read():
        clear()
        display.set_pen(WHITE)
        display.text("<-", 100, 50, 240, 4)
        display.set_pen(YELLOW)
        display.text("STOP", 10, 15, 240, 2)
        display.update()
        while True:
            motion(1, 0.002)
            if button_a.read():
                break
        sleep(1)
        clear()
    elif button_b.read():
        clear()
        display.set_pen(WHITE)
        display.text("<---", 100, 50, 240, 4)
        display.set_pen(YELLOW)
        display.text("STOP", 10, 15, 240, 2)
        display.update()
        while True:
            motion(1, 0.001)
            if button_a.read():
                break
        sleep(1)
        clear()
    elif button_x.read():
        clear()
        display.set_pen(WHITE)
        display.text("->", 100, 50, 240, 4)
        display.set_pen(YELLOW)
        display.text("STOP", 10, 15, 240, 2)
        display.update()
        while True:
            motion(0, 0.002)
            if button_a.read():
                break
        sleep(1)
        clear()
    elif button_y.read():
        clear()
        display.set_pen(WHITE)
        display.text("--->", 100, 50, 240, 4)
        display.set_pen(YELLOW)
        display.text("STOP", 10, 15, 240, 2)
        display.update()
        while True:
            motion(0, 0.001)
            if button_a.read():
                break
        sleep(1)
        clear()
    else:
        display.set_pen(GREEN)
        display.text("<-", 10, 13, 240, 4)
        display.text("<---", 10, 73, 240, 4)
        display.text("->", 200, 13, 240, 4)
        display.text("--->", 170, 73, 240, 4)
        display.update()
    sleep(0.1)  # this number is how frequently the Pico checks for button presses