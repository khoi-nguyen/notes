from random import randint

def pick(ranges, level, rand_int=True):
    key = max([n for n in ranges.keys() if n <= level])
    if rand_int:
        return randint(*ranges[key])
    else:
        return ranges[key]
