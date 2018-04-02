from random import randint
from stopwatch import StopWatch


def prefix_average1(s):
    """Return list such that, for all j, a[j] = avg(s[0], ..., s[j])."""
    n = len(s)
    a = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += s[i]
        a[j] = total / (j+1)
    return a


def prefix_average2(s):
    """Return list such that, for all j, a[j] = avg(s[0], ..., s[j])."""
    n = len(s)
    a = [0] * n
    for j in range(n):
        a[j] = sum(s[:j+1]) / (j+1)
    return a


def prefix_average3(s):
    """Return list such that, for all j, a[j] = avg(s[0], ..., s[j])."""
    n = len(s)
    a = [0] * n
    total = 0
    for j in range(n):
        total += s[j]
        a[j] = total / (j+1)
    return a


if __name__ == '__main__':
    n = 1000
    elapsed_time = []
    for j in range(4):
        s = [randint(0, 100) for i in range(n)]
        watch = StopWatch()
        prefix_average3(s)
        elapsed_time += [watch.elapsed()]
        print(n, elapsed_time[j],
              elapsed_time[j]/elapsed_time[j-1] if j > 0 else None)
        n *= 2