# generated by mBlock5 for CyberPi
# codes make you happy

import event, time, cyberpi, mbuild, mbot2

@event.start
def on_start():
    cyberpi.console.println("Hallo Philipp!")
    cyberpi.console.print("Bitte  bot auf Boden und Taste A pressen!")

@event.is_press('a')
def is_btn_press():
    while True:
      while not mbuild.ultrasonic2.get(1) < 10:
        mbot2.forward(50)
      cyberpi.audio.play_music(60, 1)
      mbot2.straight(-15)
      mbot2.turn(-90)
      

@event.is_waveleft
def on_is_waveleft():
    Test = 0
    while not Test > 5:
      cyberpi.led.on(255, 187, 0, "all")
      time.sleep(0.25)
      cyberpi.led.on(0, 0, 0, "all")
      my_10 = my_10 + 1

@event.is_waveright
def on_is_waveright():
    Test = 0
    while not Test > 5:
      cyberpi.led.on(255, 187, 0, "all")
      time.sleep(0.25)
      cyberpi.led.on(0, 0, 0, "all")
      my_10 = my_10 + 1

