def print_3d_set(s):
    min_z, max_z = min(s, key=lambda k: k[2])[2], max(s, key=lambda k: k[2])[2]
    min_y, max_y = min(s, key=lambda k: k[1])[1], max(s, key=lambda k: k[1])[1]
    min_x, max_x = min(s, key=lambda k: k[0])[0], max(s, key=lambda k: k[0])[0]

    for z in range(min_z, max_z + 1):
        print()
        print('z =', z)
        for y in range(min_y, max_y + 1):
            print(*('#' if (x, y, z) in s else '.' for x in range(min_x, max_x + 1)), sep='')


def print_4d_set(s):
    min_w, max_w = min(s, key=lambda k: k[3])[3], max(s, key=lambda k: k[3])[3]
    min_z, max_z = min(s, key=lambda k: k[2])[2], max(s, key=lambda k: k[2])[2]
    min_y, max_y = min(s, key=lambda k: k[1])[1], max(s, key=lambda k: k[1])[1]
    min_x, max_x = min(s, key=lambda k: k[0])[0], max(s, key=lambda k: k[0])[0]

    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            print()
            print('z = {}, w = {}'.format(z, w))
            for y in range(min_y, max_y + 1):
                print(*('#' if (x, y, z, w) in s else '.' for x in range(min_x, max_x + 1)), sep='')


def neighbor_counter(s):
    neighbors = {}

    for cube in s:
        for z in range(cube[2] - 1, cube[2] + 2):
            for y in range(cube[1] - 1, cube[1] + 2):
                for x in range(cube[0] - 1, cube[0] + 2):
                    if cube == (x, y, z):
                        continue
                    neighbors.setdefault((x, y, z), 0)
                    neighbors[(x, y, z)] += 1

    return neighbors


def neighbor_counter_4d(s):
    neighbors = {}

    for cube in s:
        for w in range(cube[3] - 1, cube[3] + 2):
            for z in range(cube[2] - 1, cube[2] + 2):
                for y in range(cube[1] - 1, cube[1] + 2):
                    for x in range(cube[0] - 1, cube[0] + 2):
                        if cube == (x, y, z, w):
                            continue
                        neighbors.setdefault((x, y, z, w), 0)
                        neighbors[(x, y, z, w)] += 1

    return neighbors

# Part 1
active_cubes = set()

with open("Dimension") as dim_txt:
    for y, row in enumerate(dim_txt.read().split()):
        for x, val in enumerate(row):
            if val == '#':
                active_cubes.add((x, y, 0))

for i in range(6):

    # print_3d_set(active_cubes)

    neighbor_dict = neighbor_counter(active_cubes)

    next_step_cubes = set()

    for n in neighbor_dict:
        if neighbor_dict[n] == 3 or neighbor_dict[n] == 2 and n in active_cubes:
            next_step_cubes.add(n)

    active_cubes = next_step_cubes

print(len(active_cubes))


# Part 2
active_cubes = set()

with open("Dimension") as dim_txt:
    for y, row in enumerate(dim_txt.read().split()):
        for x, val in enumerate(row):
            if val == '#':
                active_cubes.add((x, y, 0, 0))

for i in range(6):

    # print_4d_set(active_cubes)

    neighbor_dict = neighbor_counter_4d(active_cubes)

    next_step_cubes = set()

    for n in neighbor_dict:
        if neighbor_dict[n] == 3 or neighbor_dict[n] == 2 and n in active_cubes:
            next_step_cubes.add(n)

    active_cubes = next_step_cubes

print(len(active_cubes))
