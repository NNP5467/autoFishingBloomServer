import screeninfo

from log import log

# red = (94, 23, 36)
# gray = (249, 249, 249)
# pink = (208, 172, 250)
# yellow = (31, 31, 6)


def red_in_pixels(pixels: list) -> bool:
    for pixel in pixels:
        if 90 < pixel[0] < 100 and 20 < pixel[1] < 30 and 30 < pixel[2] < 40:
            return True
    return False
def gray_in_pixels(pixels: list) -> bool:
    for pixel in pixels:
        if 245 < pixel[0] < 250 and 245 < pixel[1] < 250 and 245 < pixel[2] < 250:
            return True
    return False
def pink_in_pixels(pixels: list) -> bool:
    for pixel in pixels:
        if 205 < pixel[0] < 210 and 168 < pixel[1] < 175 and 245 < pixel[2] < 252:
            return True
    return False
def yellow_in_pixels(pixels: list) -> bool:
    for pixel in pixels:
        if 25 < pixel[0] < 33 and 25 < pixel[1] < 33 and 2 < pixel[2] < 8:
            return True
    return False


log("init monitors", 0)
monitors = screeninfo.get_monitors()
if len(monitors) > 1:
    log("Ошибка инициализации монитора: не поддерживается больше 1 монитора")
if (monitors[0].width, monitors[0].height) == (1366, 768):
    pos = [(438 + 88 * i, 351) for i in range(6)]
elif (monitors[0].width, monitors[0].height) == (1917, 1070):
    pos = [(592 + 132 * i, 471) for i in range(6)]
else:
    log("Ошибка инициализации монитора: разрешение должно быть либо 1366x768 или 1917х1070", 4)

log("init vars", 0)
is_capture = False
old_pixels = None
