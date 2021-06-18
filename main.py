####################
#   Created by Vp  #
#   17.3.2021      #
#                  #
####################
import sys, bot, keyboard
from time import sleep

try:
    BOT = bot.Bot()
    toggle_button = '+'
    enabled = False
    last_state = False
    first_time = True

    print('[AntiAFK v1.0] by Vp started, press "%s" key to start/stop bot.' % toggle_button)

    while True:
        key_down = keyboard.is_pressed(toggle_button)
        if key_down != last_state:
            last_state = key_down
            if last_state:
                enabled = not enabled
                if enabled and first_time:
                    print("\nStarting bot...")
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
