import random


def between_probs(a, b):
    a = a * 100
    b = b * 100
    result = random.randint(a, b)
    return result

def between(a, b):
    a = a
    b = b
    result = random.randint(a, b)
    return result
