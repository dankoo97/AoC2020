from time import time


def remember(seq, ith):
    spoken = {v: i for i, v in enumerate(seq)}
    last = 0

    for i in range(len(seq), ith - 1):
        if last in spoken:
            spoken[last], last = i, i - spoken[last]
        else:
            spoken[last] = i
            last = 0

    return last


start_seq = [9,12,1,4,17,0,18]

start = time()
print(remember(start_seq, 2020))
print(time() - start)

start = time()
print(remember(start_seq, 30000000))  # Takes 20 seconds
print(time() - start)
