import asyncio

import config

commands = {
    "help": ["h", "help"],
    "start_pos": ["stpos", "start_pos"],
    "end_pos": ["epos", "end_pos"],
    "set_yellow": ["syel", "set_yellow"]
}


async def cmd() -> None:
    loop = asyncio.get_event_loop()

    while True:
        user = await loop.run_in_executor(None, input, "")
        user = user.split()
        if user:
            for key, value in commands.items():
                if user[0] in value:
                    user.pop(0)
                    globals()[key](len(user), user)
                    break


def start_pos(argc: int, argv: list) -> None:
    if argc == 2:
        argv[0] = int(argv[0])
        argv[1] = int(argv[1])

        if config.s_w >= argv[0] >= 0 and config.s_h >= argv[1] >= 0:
            config.pos_0 = (argv[0], argv[1])
            config.save_settings()
            config.cmd_print("Записано!")
    elif argc >= 1 and argv[0] == "default":
        config.pos_0 = None
        config.save_settings()
        config.cmd_print("Записано!")


def end_pos(argc: int, argv: list) -> None:
    if argc == 2:
        argv[0] = int(argv[0])
        argv[1] = int(argv[1])

        if config.s_w >= argv[0] >= 0 and config.s_h >= argv[1] >= 0:
            config.pos_1 = (argv[0], argv[1])
            config.save_settings()
            config.cmd_print("Записано!")
    elif argc >= 1 and argv[0] == "default":
        config.pos_1 = None
        config.save_settings()
        config.cmd_print("Записано!")


def set_yellow(argc: int, argv: list) -> None:
    if argc == 3:
        for i in range(len(argv)):
            argv[i] = int(argv[i])
            if argv[i] > 255 and argv[i] < 0:
                return
        
        config.yellow = (argv[0], argv[1], argv[2])
        config.save_settings()
        config.cmd_print("Записано!")
    elif argc >= 1 and argv[0] == "default":
        config.yellow = (252, 213, 0)
        config.save_settings()
        config.cmd_print("Записано!")


def help(argc: int, argv: list) -> None:
    config.cmd_print("""help:
    Команда help [h]: вызывает этот текст
    Команда start_pos [stpos] <point 0 | default> <point 1 | None>: переопределяет первую точку захвата экрана (default сбросит по умолчанию)
                     Примеры:
                        start_pos 500 500
                        start_pos default
    Команда end_pos [epos] <point 0 | default> <point 1 | None>: переопределяет вторую точку захвата экрана (default сбросит по умолчанию)
                     Примеры:
                        end_pos 500 500
                        end_pos default
    Команда set_yellow [syel] <r | default> <g | None> <b | None>: переопределяет жёлтый (захватываемый) цвет (default сбросит по умолчанию)
                     Примеры:
                        set_yellow 252 213 0
                        set_yellow default""")
