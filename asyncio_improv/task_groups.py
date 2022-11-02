import asyncio
import math
import time


# Remplace asyncio.gather

async def t1():
    print(int("hello"))
    await asyncio.sleep(2)


async def t2():
    print(math.sqrt(-10))
    await asyncio.sleep(1)


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(t1())
            tg.create_task(t2())
    except* ValueError as e:
        print(e.exceptions)


if __name__ == '__main__':
    asyncio.run(main())
