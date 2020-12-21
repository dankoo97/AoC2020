class Ferry:

    directions = {
        'E': (-1, 0),
        'W': (1, 0),
        'N': (0, -1),
        'S': (0, 1),
    }

    left_right = 'WNES'

    def __init__(self, waypoint=None):
        self.location = 0, 0
        self.direction = 'E'
        self.waypoint = (-10, -1) if waypoint else None

    def move(self, direction, units):
        if direction in Ferry.directions:
            d = Ferry.directions[direction]
            if self.waypoint is not None:
                self.waypoint = self.waypoint[0] + d[0] * units, self.waypoint[1] + d[1] * units
                return

        elif direction == 'F':
            if self.waypoint is not None:
                self.location = self.location[0] + self.waypoint[0] * units, self.location[1] + self.waypoint[1] * units
                return
            d = Ferry.directions[self.direction]

        elif direction in 'LR':
            d = units // 90 * (-1 if direction == 'L' else 1)

            if self.waypoint is not None:
                for _ in range(abs(d)):
                    if direction == 'R':
                        self.waypoint = self.waypoint[1], -self.waypoint[0]
                    elif direction == 'L':
                        self.waypoint = -self.waypoint[1], self.waypoint[0]
                return

            self.direction = Ferry.left_right[
                (Ferry.left_right.index(self.direction) + d) % 4
            ]
            return

        else:
            raise ValueError

        self.location = self.location[0] + d[0] * units, self.location[1] + d[1] * units
        return

    def manhattan_distance(self):
        return sum(abs(d) for d in self.location)

    def __str__(self):
        x = abs(self.location[0]), 'East' if self.location[0] < 0 else 'West' if self.location[0] > 0 else 'Center'
        y = abs(self.location[1]), 'North' if self.location[1] < 0 else 'South' if self.location[1] > 0 else 'Center'
        w = '\nWaypoint: {}, {}'.format(*self.waypoint) if self.waypoint is not None else ''
        return 'At: {} {}, {} {}\nFacing: {}'.format(*x, *y, self.direction) + w


with open("FerryInstructions") as fi_txt:
    instructions = fi_txt.read().split()

f = Ferry(True)

for cmd in instructions:
    print(f)
    print()
    print(cmd)
    f.move(cmd[0], int(cmd[1:]))

print(f)
print()

print(f.manhattan_distance())
