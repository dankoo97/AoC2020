class Toboggan:
    def __init__(self, slope, tree_map):
        self.slope = slope
        self.tree_map = tree_map

    def count_trees_along_slope(self):
        bottom = len(self.tree_map)
        width = len(self.tree_map[0])
        x = 0
        trees = 0

        for y in range(0, bottom, self.slope[1]):
            trees += int(self.tree_map[y][x % width] == '#')
            x += self.slope[0]

        return trees

    def change_slope(self, slope):
        self.slope = slope


with open("MountainSide") as ms_txt:
    mountain_side = [m.strip() for m in ms_txt.readlines()]

    print(*mountain_side, sep='\n')

t = Toboggan((3, 1), mountain_side)

print(t.count_trees_along_slope())  # Part 1: 216

total = 1

for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    t.change_slope(slope)
    total *= t.count_trees_along_slope()

print(total)  # Part 2: 6708199680
