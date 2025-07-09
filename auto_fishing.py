import pyautogui
import keyboard

import config

from log import log


def is_fish(pixels: list) -> bool:
    if config.red_in_pixels(pixels) and (config.yellow_in_pixels(pixels) or (config.pink_in_pixels(pixels) and config.gray_in_pixels(pixels))):
        return True
    return False


def switch_capture() -> None:
    config.is_capture = not config.is_capture
    log("Захват экрана " + ("включен" if config.is_capture else "выключен"))


def fishing() -> None:
    log("fishing()", 0)
    keyboard.add_hotkey("ctrl+`", switch_capture)

    while True:
        pixels = [pyautogui.pixel(*i) for i in config.pos]
        if config.is_capture:
            if is_fish(pixels):
                if pixels != config.old_pixels:
                    log("other pixels", 0)
                    if config.yellow_in_pixels(pixels):
                        pyautogui.click(button="right")
                        pyautogui.click(button="right")
                        log("Обнаружение рыбы")
                    config.old_pixels = pixels
            else:
                config.old_pixels = None
