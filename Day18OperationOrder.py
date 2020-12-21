def solve_math1(s):
    paren = []
    vals, ops = [], []

    for i, val in enumerate(s):
        if val == '(':
            paren.append(i)
        elif val == ')':
            if len(paren) == 1:
                vals.append(solve_math1(s[paren[0] + 1: i]))
            paren.pop()
        elif val == ' ':
            continue
        elif not paren and val in '+*':
            ops.append(val)
        elif not paren:
            vals.append(int(val))

    total = vals[0]

    for v, o in zip(vals[1:], ops):
        if o == '+':
            total += v
        elif o == '*':
            total *= v

    return total


def solve_math2(s):
    paren = []
    vals, ops = [], []

    for i, val in enumerate(s):
        if val == '(':
            paren.append(i)
        elif val == ')':
            if len(paren) == 1:
                vals.append(solve_math2(s[paren[0] + 1: i]))
            paren.pop()
        elif val == ' ':
            continue
        elif not paren and val in '+*':
            ops.append(val)
        elif not paren:
            vals.append(int(val))

    try:
        addition = ops.index('+')
    except ValueError:
        addition = -1

    while addition != -1:

        vals[addition] = vals[addition] + vals[addition + 1]
        del vals[addition + 1]
        del ops[addition]

        try:
            addition = ops.index('+', addition)
        except ValueError:
            addition = -1

    total = vals[0]

    for v in vals[1:]:
        total *= v

    return total


with open("Homework") as hw_txt:
    hw = hw_txt.read().splitlines()
    print(sum([solve_math1(s) for s in hw]))
    print(sum([solve_math2(s) for s in hw]))
