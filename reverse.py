from ..stack import Stack


def reverse(src, dest):
    """Overwrite given file with its contents line-by-line reversed."""
    s = Stack()
    for line in open(src):
        s.push(line.rstrip('\n'))

    out = open(dest, 'w')
    while not s.is_empty():
        out.write(s.pop() + '\n')


if __name__ == '__main__':
    reverse('stack.py', 'temp.txt')
