import re

with open("Messages") as mess_txt:
    rules_, codes = mess_txt.read().split('\n\n')

rules = {}
for r in rules_.splitlines():
    rules[int(r.split(':')[0])] = r.split(':')[1].strip(' "')

end_rule = rules[0]

while any(c.isdigit() for c in end_rule):
    x = end_rule.split()
    for i, v in enumerate(x):
        if v.isdigit():
            x[i] = '( {} )'.format(rules[int(v)])
    end_rule = ' '.join(x)

end_rule = ''.join(end_rule.split())
# print(end_rule)

match = re.compile(r'^' + end_rule + r'$')
cnt = 0

for c in codes.split():
    if re.match(match, c):
        cnt += 1

print(cnt)  # Part 1



### PART 2 ###

end_rule = rules[0]

while any(c.isdigit() for c in end_rule):
    try:
        x = end_rule.split()
        for i, v in enumerate(x):
            if v.isdigit():
                if v == '8':
                    x[i] = '( {} )+'.format(rules[42])
                elif v == '11':
                    x[i] = f'( ( {rules[42]} )x( {rules[31]} )x )'
                else:
                    x[i] = '( {} )'.format(rules[int(v)])
        end_rule = ' '.join(x)
    except KeyboardInterrupt:
        break

end_rule = ''.join(end_rule.split()).replace('x', '{x}')

cnt = 0
for i in range(1, 10):
    end_rule = end_rule.replace('{x}', '{' + str(i) + '}')

    # print(end_rule)
    # print()

    match = re.compile(r'^' + end_rule + r'$')

    for c in codes.split():
        if re.match(match, c):
            cnt += 1

    end_rule = end_rule.replace('{' + str(i) + '}', '{x}')


print(cnt)  # Part 2
