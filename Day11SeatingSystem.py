class Lobby:

    def __init__(self, seat_list):
        self.seat_list = seat_list

    def flip_seat(self, row, col):
        if self.seat_list[row][col] == 2:
            raise IndexError('No seat exists there')
        self.seat_list[row][col] = int(not self.seat_list[row][col])

    def should_seat_flip(self, row, col, max_seats=None):
        if self.seat_list[row][col] == 2:
            raise IndexError('No seat exists there')

        if not self.seat_list[row][col]:
            for _dir in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):

                r, c = _dir

                try:
                    while row + r >= 0 and col + c >= 0:
                        if self.seat_list[row + r][col + c] == 1:
                            return False
                        if self.seat_list[row + r][col + c] == 0:
                            break
                        r, c = r + _dir[0], c + _dir[1]
                except IndexError:
                    pass

            return True

        cnt = 0
        for _dir in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):

            r, c = _dir

            try:
                while row + r >= 0 and col + c >= 0:
                    if self.seat_list[row + r][col + c] in (0, 1):
                        cnt += self.seat_list[row + r][col + c]
                        break
                    r, c = r + _dir[0], c + _dir[1]
            except IndexError:
                pass

        if max_seats is None:
            max_seats = 4

        return cnt >= max_seats

    def one_step(self, max_seats=None):
        if max_seats is None:
            max_seats = 4

        new_seats = []
        f = False

        for row in range(len(self.seat_list)):
            new_seats.append([])

            for col in range(len(self.seat_list[row])):
                try:
                    if self.should_seat_flip(row, col, max_seats):
                        new_seats[-1].append(int(not self.seat_list[row][col]))
                        f = True

                    else:
                        new_seats[-1].append(self.seat_list[row][col])

                except IndexError:
                    new_seats[-1].append(2)

        self.seat_list = new_seats
        return f

    def run(self, prints=None, max_seats=None):
        if max_seats is None:
            max_seats = 4

        flag = self.one_step(max_seats)

        while flag:
            if prints:
                print(self)
            flag = self.one_step(max_seats)

        if prints:
            print(self)

        return sum([row.count(1) for row in self.seat_list])

    def __str__(self):
        s = ''

        key_guide = {
            0: 'L',
            1: '#',
            2: '.',
        }

        for row in self.seat_list:
            s += ''.join(key_guide[c] for c in row) + '\n'

        return s

    lobby_map_key = {
        'L': 0,
        '#': 1,
        '.': 2,
    }


with open("WaitingArea") as wa_txt:
    lobby_map = [[Lobby.lobby_map_key[s] for s in row] for row in wa_txt.read().split()]


lobby = Lobby(lobby_map)
print(lobby.run(False, 5))
