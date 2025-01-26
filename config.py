import screeninfo
import asyncio
import pyautogui

import os
import json


def save_settings():
    with open(os.path.join(path, "config.json"), "w", encoding="utf-8-sig") as file:
        json.dump({
            "pos_0": pos_0,
            "pos_1": pos_1,
            "yellow": yellow,
            "delay": delay
        }, file, indent=4)


def cmd_print(*args: object, **kwargs: object) -> None:
    print(">", *args, **kwargs)


async def is_fish():
    global fish
    while True:
        await asyncio.sleep(0.01)
        if fish:
            await asyncio.sleep(5)
            pyautogui.click(button="right")
            fish = False
            print("ok")


path = os.path.join(os.getenv("APPDATA"), "autoFishingBloomServer")
os.makedirs(path, exist_ok=True)

monitor = screeninfo.get_monitors()[0]

s_w = monitor.width
s_h = monitor.height

pos_0 = (s_w / 2 - s_w * 0.26, s_h / 2 - s_h * 0.15)
pos_1 = (s_w / 2 + s_w * 0.26, s_h / 2)
yellow = (252, 213, 0)
delay = 0

detect = False
fish = False

try:
    with open(os.path.join(path, "config.json"), "r", encoding="utf-8-sig") as file:
        file = json.load(file)
        pos_0 = file["pos_0"]
        pos_1 = file["pos_1"]
        yellow = file["yellow"]
        delay = file["delay"]
except FileNotFoundError:
    pass
