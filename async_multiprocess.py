import asyncio
import sys
import time

import aiohttp
import async_timeout


async def hold(sec):
    print(f'Running for {sec} seconds')
    await asyncio.sleep(sec)


async def main():
    times = [2, 3, 4]
    tasks = []

    for seconds in times:
        task = asyncio.ensure_future(hold(seconds))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    _start = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(main())
    loop.run_until_complete(future)
    print(f"Execution time: { time.time() - _start }")
    loop.close()
