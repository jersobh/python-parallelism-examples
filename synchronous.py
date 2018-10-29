import time

def hold(sec):
    print(f'Running for {sec} seconds')
    return time.sleep(sec)

def main():
    _start = time.time()
    times = [2,3,4]
    for seconds in times:
        hold(seconds)

    print(f"Execution time: { time.time() - _start }")

if __name__ == '__main__':
    main()
