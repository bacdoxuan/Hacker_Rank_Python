class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())
    stream.__init__()

"""
This program works like below:
1. Enter the number of times that print stream (even or odd), input: int
2. Enter 2 factors:
 - first, enter "odd" or "even", input: str
 - second, the number of odd or even number will be print, intput: int
Example:
3
odd 3
even 5
odd 5

"""
queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())