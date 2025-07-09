import colorama

colorama.init()

import auto_fishing

from log import log

if __name__ == "__main__":
    print("Auto Fishing Bloom Server (v 2.0)")
    print("Для запуска и выключения захвата экрана нажмите ctrl+` (ctrl+ё)")
    print("В данной версии отсутствует консоль из-за отсутствия файла с настройками")
    print("Программа должна ОБЯЗАТЕЛЬНО запускаться на английской раскладке")
    try:
        log("start", 0)
        auto_fishing.fishing()
    except KeyboardInterrupt:
        log("Завершение программы")
    except Exception as e:
        log("Произошла непредвиденная ошибка. Отправьте скриншот ошибки и обстоятельства, при которых она произошла, разработчику ПО\nОшибка: " + str(e), 4)
