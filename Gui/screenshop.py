import time
import keyboard
from PIL import ImageGrab


def screenshop():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey('F9', screenshop)
# keyboard.add_hotkey('a', screenshop)
# keyboard.add_hotkey('ctrl+shift+s', screenshop)

keyboard.wait('esc')
