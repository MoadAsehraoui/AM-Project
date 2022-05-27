from microbit import *
import music

steps=0
display.scroll(steps)
calories = 0
distance = 0
counter = 0
counter2 = 0
speed = 0
time1 = running_time()

while True:
    if accelerometer.get_y() > 1000:
        steps += 1
        counter2 += 1
        display.scroll(steps)
    if counter2 == 10:
        calories = calories + 40.4
        distance += 0.0006
        speed = accelerometer.get_y()
        counter2 = 0
    if button_a.is_pressed():
        music.play(music.POWER_UP)
        display.scroll("restart")
        sleep(300)
        calories = 0
        distance = 0
        steps = 0
        counter = 0
        counter2 = 0
        time1 = running_time()
    if button_b.is_pressed():
        time2 = running_time()
        time = (time2 - time1)/1000
        music.play(music.POWER_DOWN)
        display.scroll("Duration:")
        display.scroll(time)
        sleep(300)
        display.scroll("steps:")
        display.scroll(steps)
        sleep(300)
        display.scroll("speed:")
        display.scroll(speed)
        sleep(300)
        display.scroll("calories:")
        display.scroll(calories)
        sleep(300)