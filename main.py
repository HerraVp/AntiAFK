####################
#   Created by Vp  #
#   17.3.2021      #
#                  #
####################


import sys, bot, keyboard
import time

v = "v1.1"

print("===================================")
print("Made by https://github.com/HerraVp")
print("===================================")
time.sleep(2)

try:
    BOT = bot.Bot()
    toggle_button = '+'
    enabled = False
    last_state = False
    first_time = True

    print(f'[AntiAFK {v} by Vp] Started, press "%s" key to start/stop bot.' % toggle_button)

    while True:
        key_down = keyboard.is_pressed(toggle_button)
        if key_down != last_state:
            last_state = key_down
            if last_state:
                enabled = not enabled
                if enabled and first_time:
                    print(f"\n[AntiAFK {v} by Vp] Starting bot...")
                    BOT.start()
                    first_time = False
                elif enabled:
                    BOT.resume()
                else:
                    BOT.pause()
except SystemExit:
    pass
except KeyboardInterrupt:
    sys.exit()
