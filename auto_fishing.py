import asyncio
import pyautogui
import keyboard

import config

from PIL import ImageGrab
from config import s_w, s_h


async def main() -> None:
    run = False
    while True:
        await asyncio.sleep(0.01)
        if keyboard.is_pressed("F4"):
            run = not run

        if config.auto_fishing_running and run:
            # start_pos = (s_w / 2 - s_w * 0.26, s_h / 2 - s_h * 0.15)
            # end_pos = (s_w / 2 + s_w * 0.26, s_h / 2)

            # screenshot = ImageGrab.grab((*start_pos, *end_pos))
            # screenshot.save(".\\screenshot.png")
            # break
            pass
