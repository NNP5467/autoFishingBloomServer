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
                start_pos = (s_w / 2 - s_w * 0.26, s_h / 2 - s_h * 0.13)
            else:
                start_pos = config.pos_0
            if config.pos_1 is None:
                end_pos = (s_w / 2 + s_w * 0.26, s_h / 2 - s_h * 0.09)
            else:
                end_pos = config.pos_1

            screenshot = ImageGrab.grab((*start_pos, *end_pos))
            
            try:
                for i in screenshot.getcolors(1000000):
                    rgb = i[1]
                    if rgb == config.yellow:
                        config.fish = True
                        pyautogui.click(button="right")
                        cmd_print("Обнаружил жёлтый цвет!")
                        break

            except TypeError:
                cmd_print("Произошла непредвиденная ошибка. Если это критически повлияло на "
                          "работу программы, пожалуйста, отправьте скриншот ошибки и "
                          "обстоятельства, при которых она произошла, разработчику ПО. \n", "TypeError")
