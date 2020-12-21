class Handheld:

    def __init__(self, instructions):
        self.instructions = [(c.split()[0], int(c.split()[1])) for c in instructions.split('\n')]
        self.pos, self.acc = 0, 0
        self.visited = set()
        self.instruction_length = len(self.instructions)

    def accumulate(self, n):
        self.acc += n
        self.pos += 1

    def jump(self, n):
        self.pos += n

    def no_operation(self, n):
        self.pos += 1

    def reset(self):
        self.pos, self.acc = 0, 0
        self.visited = set()

    def run(self):
        while 0 <= self.pos < self.instruction_length:
            cmd, vals = self.instructions[self.pos]
            if self.pos in self.visited:
                return self.acc
            self.visited.add(self.pos)
            Handheld.static_instructions[cmd](self, int(vals))

    def fix(self):
        for i in range(self.instruction_length):

            if self.instructions[i][0] in ('jmp', 'nop'):
                if self.instructions[i][0] == 'jmp':
                    self.instructions[i] = 'nop', self.instructions[i][1]
                elif self.instructions[i][0] == 'nop':
                    self.instructions[i] = 'jmp', self.instructions[i][1]

                if self.run() is None:
                    return self.acc

                if self.instructions[i][0] == 'jmp':
                    self.instructions[i] = 'nop', self.instructions[i][1]
                elif self.instructions[i][0] == 'nop':
                    self.instructions[i] = 'jmp', self.instructions[i][1]

                self.reset()

    static_instructions = {
        'jmp': jump,
        'acc': accumulate,
        'nop': no_operation,
    }


with open("HandheldCode") as hh_txt:
    t = hh_txt.read().strip()
    hh = Handheld(t)

print(hh.run())  # Part 1
hh.reset()
print(hh.fix())  # Part 2
