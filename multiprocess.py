import time
from multiprocessing import Process

def hold(sec):
    print(f'Running for {sec} seconds')
    return time.sleep(sec)

def main():
    _start = time.time()
    times = [2, 3, 4]
    processes = []
    for seconds in times:
        process = Process(target=hold, args=(seconds,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f"Execution time: { time.time() - _start }")

if __name__ == '__main__':
    main()
