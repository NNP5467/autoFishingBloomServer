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
    asyncio.run(main())
