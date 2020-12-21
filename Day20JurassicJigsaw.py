class Tile:
    def __init__(self, id_, image):
        self.id_ = id_
        self.image = []
        for row in image.splitlines():
            self.image.append([])
            for v in row:
                self.image[-1].append(v == '#')
        self.neighbors = set()
        self.edges = {
            tuple(self.image[0]),
            tuple(self.image[-1]),
            tuple(self.image[i][0] for i in range(len(self.image))),
            tuple(self.image[i][-1] for i in range(len(self.image))),
            tuple(self.image[0])[::-1],
            tuple(self.image[-1])[::-1],
            tuple(self.image[i][0] for i in range(len(self.image)))[::-1],
            tuple(self.image[i][-1] for i in range(len(self.image)))[::-1],
        }

        self.edges_with_neighbor = set()

    def __str__(self):
        s = ''

        for row in self.image:
            s += '\n'
            for v in row:
                s += '#' if v else '.'

        return s.strip()

    def __repr__(self):
        return str(self)

    def compare_edges(self, other):
        s = self.edges & other.edges
        if s:
            self.neighbors.add(other)
            self.edges_with_neighbor.add(next(iter(s)))

            other.neighbors.add(self)
            other.edges_with_neighbor.add(next(iter(s)))
        return s

    def __hash__(self):
        return hash(tuple(e for e in self.edges))

    def __eq__(self, other):
        return self.image == other.image and self.id_ == other.id_

    def how_many_neighbors(self):
        return len(self.neighbors)

    def get_id(self):
        return self.id_

    def rotate(self):
        self.image = [[self.image[-i - 1][j] for i in range(len(self.image))] for j in range(len(self.image))]

    def flip(self):
        self.image = self.image[::-1]

    def check_rotations(self):
        for _ in range(4):
            self.rotate()
            yield self

        self.flip()

        for _ in range(4):
            self.rotate()

            yield self

        self.flip()

    def search_tile(self, search_pattern):

        new_image = []
        for s in str(self).splitlines():
            new_image.append(list(s))

        def search_at(x, y):

            coords = []

            for i in range(len(search_pattern)):
                for j in range(len(search_pattern[0])):
                    if search_pattern[i][j] == ' ':
                        continue
                    if new_image[y + i][x + j] == '.':
                        return []
                    coords.append((x + j, y + i))

            return coords

        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                try:
                    o_ = search_at(j, i)
                except IndexError:
                    break
                for coord in o_:
                    new_image[coord[1]][coord[0]] = 'O'

        return new_image


def combine_tiles(c):
    def find_next_tile(tile, pattern, direction):
        try:
            next_tile = [neighbor for neighbor in tile.neighbors if {pattern, pattern[::-1]} & neighbor.edges][0]
        except IndexError:
            raise ValueError('Missing Neighbor')  # One

        if direction == 'r':
            for neighbor in next_tile.check_rotations():
                if tuple(neighbor.image[i][0] for i in range(len(neighbor.image))) == tuple(
                        tile.image[i][-1] for i in range(len(tile.image))):
                    return neighbor

            raise ValueError('Failed Neighbor')

        if direction == 'd':
            for neighbor in next_tile.check_rotations():
                if tuple(neighbor.image[0]) == tuple(tile.image[-1]):
                    return neighbor

            raise ValueError('Failed Neighbor')

        raise ValueError('Incorrect or no direction. Given: {}'.format(direction))

    tile_pattern = [[]]

    # top left corner
    for rot in c.check_rotations():
        if len([r for r in [
                tuple(rot.image[-1]),
                tuple(rot.image[-1])[::-1],
                tuple(rot.image[i][-1] for i in range(len(rot.image))),
                tuple(rot.image[i][-1] for i in range(len(rot.image)))[::-1],
        ] if r in c.edges_with_neighbor]) == 2:
            c = rot
            break
    else:
        raise ValueError('Failed top left corner')


    # Top Row
    tile_pattern[-1].append(c)
    next_tile = find_next_tile(c, tuple(c.image[i][-1] for i in range(len(c.image))), 'r')
    tile_pattern[-1].append(next_tile)
    c = next_tile

    while len(next_tile.edges_with_neighbor) > 2:
        next_tile = find_next_tile(c, tuple(c.image[i][-1] for i in range(len(c.image))), 'r')
        tile_pattern[-1].append(next_tile)
        c = next_tile

    tile_pattern.append([])
    c = find_next_tile(tile_pattern[0][0], tuple(tile_pattern[0][0].image[-1]), 'd')

    # Middle Rows
    while len(c.edges_with_neighbor) > 2:

        tile_pattern[-1].append(c)
        next_tile = find_next_tile(c, tuple(c.image[i][-1] for i in range(len(c.image))), 'r')
        tile_pattern[-1].append(next_tile)
        c = next_tile

        while len(next_tile.edges_with_neighbor) > 3:
            try:
                next_tile = find_next_tile(c, tuple(c.image[i][-1] for i in range(len(c.image))), 'r')
                tile_pattern[-1].append(next_tile)
                c = next_tile
            except ValueError:
                break

        tile_pattern.append([])
        c = find_next_tile(tile_pattern[-2][0], tuple(tile_pattern[-2][0].image[-1]), 'd')

    # Bottom Row
    tile_pattern[-1].append(c)
    next_tile = find_next_tile(c, tuple(c.image[i][-1] for i in range(len(c.image))), 'r')
    tile_pattern[-1].append(next_tile)
    c = next_tile

    while len(next_tile.edges_with_neighbor) > 2:
        next_tile = find_next_tile(c, tuple(c.image[i][-1] for i in range(len(c.image))), 'r')
        tile_pattern[-1].append(next_tile)
        c = next_tile

    return tile_pattern


def tile_pattern_to_string(tile_pattern):
    s = ''
    for tile_row in tile_pattern:
        for row in range(1, len(tile_row[0].image) - 1):
            for tile in range(len(tile_row)):
                s += ''.join('#' if t else '.' for t in tile_row[tile].image[row][1:-1])
            s += '\n'

    return s


with open("TileText") as t_txt:
    tiles = t_txt.read().split('\n\n')

my_tiles = {}
for t in tiles:
    name, image = t.split(':')
    my_tiles[name[5:]] = (Tile(int(name[5:]), image.strip()))

for t in my_tiles:
    for other in my_tiles:
        if t == other:
            continue
        if my_tiles[t].how_many_neighbors() == 4:
            break
        Tile.compare_edges(my_tiles[t], my_tiles[other])

corners = [my_tiles[t].get_id() for t in my_tiles if my_tiles[t].how_many_neighbors() == 2]

p = 1
for c in corners:
    p *= c

print(p)  # Part 1
print()


tile_pattern = combine_tiles(my_tiles[str(corners[0])])
print()


test = tile_pattern_to_string(tile_pattern)

# We can use our tile rotation and flip functions if we combine all the tiles to one large one
full_image = Tile(-1, test)

search_pattern = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.strip('\n').splitlines()

print()

for rot in full_image.check_rotations():
    s = '\n'.join(''.join(y) for y in rot.search_tile(search_pattern))
    if 'O' in s:
        print(s.replace('O', u'\u2588').replace('.', ' ').replace('#', u'\u2591'))
        print(s.count('#'))  # Part 2
