from random import randint
from stopwatch import StopWatch


def unique1(s):
    """Return True is there are no duplicate elements in sequence s."""
    for j in range(len(s)):
        for k in range(j+1, len(s)):
            if s[j] == s[k]:
                return False
    return True


def unique2(s):
    """Return True is there are no duplicate elements in sequence s."""
    temp = sorted(s)
    for j in range(1, len(s)):
        if s[j-1] == s[j]:
                return False
    return True


if __name__ == '__main__':
    n = 20
    elapsed_time = []
    for j in range(4):
        s = [randint(0, 10000) for i in range(n)]
        watch = StopWatch()
        unique2(s)
        elapsed_time += [watch.elapsed()]
        print(n, elapsed_time[j],
              elapsed_time[j]/elapsed_time[j-1] if j > 0 else None)
        n *= 2