from random import randint
from stopwatch import StopWatch


def disjoint1(a, b, c):
    """Return True is there is no element common to all three lists."""
    for i in a:
        for j in b:
            for k in c:
                if a == b == c:
                    return False
    return True


def disjoint2(a, b, c):
    """Return True is there is no element common to all three lists."""
    for i in a:
        for j in b:
            if a == b:
                for k in c:
                    if a == c:
                        return False
    return True


if __name__ == '__main__':
    n = 20
    elapsed_time = []
    for j in range(4):
        a = [randint(0, 100) for i in range(n)]
        b = [randint(0, 100) for i in range(n)]
        c = [randint(0, 100) for i in range(n)]
        watch = StopWatch()
        disjoint2(a, b, c)
        elapsed_time += [watch.elapsed()]
        print(n, elapsed_time[j],
              elapsed_time[j]/elapsed_time[j-1] if j > 0 else None)
        n *= 2