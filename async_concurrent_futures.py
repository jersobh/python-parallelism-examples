import asyncio
import time
import concurrent.futures


def hold(n):
    print(f'Running task number {n}')
    return n


async def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(hold, i) for i in range(5)}
        for future in concurrent.futures.as_completed(futures):
            data = future.result()
            print(data)


if __name__ == '__main__':
    _start = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(main())
    loop.run_until_complete(future)
    print(f"Execution time: { time.time() - _start }")
    loop.close()
