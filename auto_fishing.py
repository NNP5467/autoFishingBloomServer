import asyncio
import pyautogui
import keyboard

import config

from PIL import ImageGrab
from config import pos_0, pos_1, cmd_print


def d():
    config.detect = not config.detect
    cmd_print("Захват экрана", "включен" if config.detect else "выключен")


async def main() -> None:
    keyboard.add_hotkey("ctrl+`", d)

    while True:
        await asyncio.sleep(0.01)

        if config.detect:
            screenshot = ImageGrab.grab((*pos_0, *pos_1))
            
            try:
                for i in screenshot.getcolors(1000000):
                    rgb = i[1]
                    if rgb == config.yellow:
                        config.fish = True
                        pyautogui.click(button="right")
                        cmd_print("Обнаружил жёлтый цвет!")
                        await asyncio.sleep(config.delay)
                        break

            except TypeError:
                cmd_print("Произошла непредвиденная ошибка. Если это критически повлияло на "
                          "работу программы, пожалуйста, отправьте скриншот ошибки и "
                          "обстоятельства, при которых она произошла, разработчику ПО. \n", "TypeError")
