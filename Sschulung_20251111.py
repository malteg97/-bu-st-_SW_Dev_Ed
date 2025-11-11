# Startkommentar

import event, time, cyberpi, mbot2

@event.start
def on_start():
    mbot2.forward(50, 3)
    mbot2.turn(-90)
    mbot2.forward(50, 3)
    mbot2.turn(90)
    mbot2.forward(50, 1)