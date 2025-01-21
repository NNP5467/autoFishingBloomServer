import screeninfo


def cmd_print(*args: object, **kwargs: object) -> None:
    print(">", *args, **kwargs)


monitor = screeninfo.get_monitors()[0]

pos_0 = None
pos_1 = None

s_w = monitor.width
s_h = monitor.height
