from random import randint

def pick(ranges, level):
    key = max([n for n in ranges.keys() if n <= level])
    return randint(*ranges[key])
