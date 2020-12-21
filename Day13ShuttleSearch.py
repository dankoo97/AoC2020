import math

with open("BusList") as bl_txt:
    time, busses = bl_txt.read().split()

    time = int(time)
    busses = [int(b) if b != 'x' else 0 for b in busses.split(',') ]

earliest = time
bus_id = time

for bus in [b for b in busses if b != 0]:
    if bus - (time % bus) < earliest:
        earliest = bus - (time % bus)
        bus_id = bus

# print(earliest * bus_id)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def find_subsequent_stops(busses):
    inc = max(busses)
    pos = busses.index(inc)
    s = inc

    vec = [(inc + v + i - pos) % v if v else 0 for i, v in enumerate(busses)]
    inc_vec = [not b for b in busses]
    inc_vec[pos] = True

    for i in range(len(inc_vec)):
        if inc_vec[i] == bool(vec[i]):
            inc_vec[i] = not inc_vec[i]
            inc *= busses[i]

    print(s)
    print(vec)
    print()

    while any(vec):
        s += inc
        vec = [(v + inc) % busses[i] if v else 0 for i, v in enumerate(vec)]
        for i in range(len(inc_vec)):
            if inc_vec[i] == bool(vec[i]):
                inc_vec[i] = not inc_vec[i]
                inc *= busses[i]

        print(s)
        print(vec)
        print()

    return s - pos


check = find_subsequent_stops(busses)

print(check)

# for i in range(check, check + len(busses)):
#     if busses[i - check]:
#         print(busses[i-check], ':', i % busses[i - check])
