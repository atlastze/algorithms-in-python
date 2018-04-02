from time import time


class StopWatch:
    def __init__(self):
        self.start_time = time()

    def start(self):
        self.start_time = time()
        return self.start_time

    def elapsed(self):
        return time() - self.start_time


if __name__ == '__main__':
    from time import sleep
    watch = StopWatch()
    sleep(0.2)
    print(watch.elapsed())
