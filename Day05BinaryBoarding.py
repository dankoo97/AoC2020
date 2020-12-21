class Airplane:
    def __init__(self, rows, columns):
        self.row = rows
        self.col = columns
        self.seats = [[True for _ in range(columns)] for __ in range(rows)]

    def seat_taken(self, seat_code):
        seat = [[0, self.row], [0, self.col]]

        for i in range(7):
            if seat_code[i] == 'F':
                seat[0][1] -= (seat[0][1] - seat[0][0]) // 2
            elif seat_code[i] == 'B':
                seat[0][0] += (seat[0][1] - seat[0][0]) // 2

        for j in range(-3, 0):
            if seat_code[j] == 'L':
                seat[1][1] -= (seat[1][1] - seat[1][0]) // 2
            elif seat_code[j] == 'R':
                seat[1][0] += (seat[1][1] - seat[1][0]) // 2

        self.seats[seat[0][1] - 1][seat[1][1] - 1] = False

        return seat[0][1] - 1, seat[1][1] - 1

    def available_seats(self):
        s = []
        for i in range(self.row):
            for j in range(self.col):
                if self.seats[i][j]:
                    s.append((i, j))

        return s


ap = Airplane(128, 8)
my_bp = []
with open("BoardingPasses") as bp_txt:
    for bp in bp_txt.read().split():
        my_bp.append(ap.seat_taken(bp))

# ap.seat_taken('BFFFBBFRRR')

print(*ap.seats, sep='\n')
max_ = max(my_bp, key=lambda rc: rc[0] * 8 + rc[1])

print(max_[0] * 8 + max_[1])  # Part 1: 861

free_seats = ap.available_seats()

for s in free_seats:
    if all((s[0], s[1] + i) not in free_seats for i in (-1, 1)):
        print(s[0] * 8 + s[1])  # Part 2: 633
