# generated by mBlock5 for CyberPi
# codes make you happy

import event, time, cyberpi, mbot2


@event.is_press('a')
def is_btn_press():
    mbot2.forward(50, 3)
    mbot2.turn(-90)
    mbot2.forward(50, 3)
    mbot2.turn(90)
    mbot2.forward(50, 3)


@event.is_anticlockwise
def on_is_anticlockwise():
    for count in range(3):
      cyberpi.led.on(208, 170, 1, 5)
      time.sleep(0.2)
      cyberpi.led.on(0, 0, 0, 5)
      time.sleep(0.2)


@event.start
def on_start():
    cyberpi.console.println("Willkommen!")
    cyberpi.console.println(cyberpi.get_battery())
    cyberpi.console.println("Zum Start Taste A Drücken")


@event.is_clockwise
def on_is_clockwise1():
    for count2 in range(3):
      cyberpi.led.on(208, 170, 1, 1)
      time.sleep(0.2)
      cyberpi.led.on(0, 0, 0, 1)
      time.sleep(0.2)