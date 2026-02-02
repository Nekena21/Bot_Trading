import time

last_signal_time = 0


def cooldown():
    global last_signal_time
    if time.time() - last_signal_time < 60:
        return False
    last_signal_time = time.time()
    return True
