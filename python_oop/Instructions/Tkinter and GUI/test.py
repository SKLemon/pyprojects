def add(*args):
    list = [number for number in args]
    total = sum(list)
    return total


"""
? Best solution is:
# def add(*args):
# return sum(args)
? This is because *args stores the input as a tuple... and a tuple is iterable with sum()
"""

add(2, 3, 5)


def calculator(**kwargs):
    for key, value in kwargs.items():
        print(key)
        value += 1
        pass
