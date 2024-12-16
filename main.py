import event, time, cyberpi

@event.start
def on_start():
    cyberpi.console.println("Hallo Philipp")