import asyncio

import config

from msvcrt import getch

commands = {
    "help": ["h", "help"],
    "tts": ["tts", "text-to-speech"],
    "start": ["st", "start"],
    "end": ["end"]
}


def cmd_print(*args: object, **kwargs: object) -> None:
    print("> ", *args, **kwargs)


async def cmd() -> None:
    loop = asyncio.get_event_loop()

    while True:
        try:
            user = await loop.run_in_executor(None, input, "")
            user = user.split()
            if user:
                for key, value in commands.items():
                    if user[0] in value:
                        user.pop(0)
                        globals()[key](len(user), user)
                        break

        except Exception as e:
            cmd_print("Error:", e)


def start(argc: int, argv: list) -> None:
    cmd_print("Авто рыбалка включена! Нажмите комбинацию клавиш для считывания экрана")
    config.auto_fishing_running = True


def end(argc: int, argv: list) -> None:
    cmd_print("Авто рыбалка выключена!")
    config.auto_fishing_running = False


def tts(argc: int, argv: list) -> None:
    if argv:
        if argv[0] == "on":
            config.tts = True
        elif argv[0] == "off":
            config.tts = False
    else:
        cmd_print("Команда tts принимает аргументы!")


def help(argc: int, argv: list) -> None:
    pass
