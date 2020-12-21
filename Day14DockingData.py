from itertools import combinations


mem = dict()
mask = []


with open("MaskInstructions") as mi_txt:
    for cmd in mi_txt.read().splitlines():
        func, val = cmd.split(' = ')
        if func.startswith('mem'):
            _index = func[4:-1]
            alter = list(bin(int(val))[2:].zfill(36))
            for i in range(36):
                if mask[i] is None:
                    continue
                else:
                    alter[i] = mask[i]
            mem[_index] = alter
        elif func.startswith('mask'):
            mask = [str(int(i)) if i != 'X' else None for i in val]

for m in mem:
    mem[m] = int('0b' + ''.join(mem[m]), 2)

print(sum(mem[m] for m in mem))


mem = dict()
mask = []


with open("MaskInstructions") as mi_txt:
    for cmd in mi_txt.read().splitlines():
        func, val = cmd.split(' = ')

        if func.startswith('mem'):
            _index = list(bin(int(func[4:-1]))[2:].zfill(36))

            for i in range(36):
                if mask[i] == '1':
                    _index[i] = mask[i]
                elif mask[i] is None:
                    _index[i] = None

            floating = tuple(35 - i for i, x in enumerate(_index) if x is None)
            _index = int('0b' + ''.join(str(int(i)) if i is not None else '0' for i in _index), 2)

            for r in range(len(floating) + 1):
                for floats in combinations(floating, r):
                    mem[_index + sum(2 ** f for f in floats)] = int(val)

        elif func.startswith('mask'):
            mask = [str(int(i)) if i != 'X' else None for i in val]


print(sum(mem.values()))
