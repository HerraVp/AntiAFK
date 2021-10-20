####################
#   Created by Vp  #
#   17.3.2021      #
#                  #
####################


import threading, time
from pynput.keyboard import Key, Controller

v = "v1.1"

def pressKey(key, controller):
    print("[AntiAFK v1.1 by Vp]: Pressing %s" % key)
    controller.press(key)
    time.sleep(3)
    # print("[BOT]: Releasing %s" % key)
    controller.release(key)


class Bot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.paused = False
        self.pause_condition = threading.Condition(threading.Lock())
        self.keys = ["w", "a", "s", "d"]
        self.keyboard = Controller()

    def run(self):
        while True:
            with self.pause_condition:
                while self.paused:
                    self.pause_condition.wait()

                pressKey(self.keys[0], self.keyboard)
                pressKey(self.keys[2], self.keyboard)

            time.sleep(3)

    def pause(self):
        print(f"\n[AntiAFK {v} by Vp]: Pausing...")
        self.paused = True
        self.pause_condition.acquire()

    def resume(self):
        print(f"[AntiAFK {v} by Vp]: Resuming...\n")
        self.paused = False
        self.pause_condition.notify()
        self.pause_condition.release()
