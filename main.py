import asyncio

import user_cmd
import auto_fishing


async def main():
    try:
        await asyncio.gather(user_cmd.cmd(), auto_fishing.main())
    except Exception as e:
        print("Произошла непредвиденная ошибка. Если это критически повлияло на "
              "работу программы, пожалуйста, отправьте скриншот ошибки и "
              "обстоятельства, при которых она произошла, разработчику ПО. \n", e)


if __name__ == "__main__":
    print("""\t\t\tAuto Fishing
Для запуска и выключения захвата экрана нажмите ctrl+` (ctrl+ё)
Для помощи по командам введите help или h""")

    asyncio.run(main())
