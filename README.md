# timelapse_slider
Motorized timelapse slider with speed and direction options

![](https://github.com/jolbertti/timelapse_slider/blob/main/ezgif.com-gif-maker.gif)

Parts needed:

- Raspberry Pi Pico
- Pimoroni Pico Display
- 28BYJ-48 5V stepper motor with the ULN2003 driver
- Battery pack between 5-12V for the motor driver, I used 8 X 1.5 V AA which was originally for a larger stepper motor
- 3.3V-5V battery for the Pico


- Slower speed: 95cm in about 4 min
- Faster speed: 95cm in about 8 min

If we wanted to make a 4 second timelapse clip with 30 fps, you could calculate the time needed for the end video like this:

(fps) * (shutter speed + delay between photos) * video length / seconds in one minute

30 * (3 + 1) * 4 / 60 = 8 (minutes)
