import asyncio
import pyautogui
import keyboard

import config

from PIL import ImageGrab
from config import s_w, s_h, cmd_print


def d():
    config.detect = not config.detect
    cmd_print("Захват экрана", "включен" if config.detect else "выключен")


async def main() -> None:
    keyboard.add_hotkey("ctrl+`", d)

    while True:
        await asyncio.sleep(0.01)

        if config.detect:
            if config.pos_0 is None:
                start_pos = (s_w / 2 - s_w * 0.26, s_h / 2 - s_h * 0.15)
            else:
                start_pos = config.pos_0
            if config.pos_1 is None:
                end_pos = (s_w / 2 + s_w * 0.26, s_h / 2)
            else:
                end_pos = config.pos_1

            screenshot = ImageGrab.grab((*start_pos, *end_pos))
            
            try:
                for coord, i in enumerate(screenshot.getcolors(256)):
                    rgb = i[1]
                    if rgb == (252, 212, 0):
                        config.fish = True
                        cmd_print("click!", f"{rgb = }  {coord = }")
                        pyautogui.click(button="right")
                        await asyncio.sleep(0.5)
                        break

            except TypeError:
                cmd_print("TypeError")
