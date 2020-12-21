with open("CustomsAnswers") as ca_txt:
    groups = [ans.split() for ans in ca_txt.read().split('\n\n')]

g_1 = groups[:]
g_2 = groups[:]
for i in range(len(groups)):
    g_1[i] = set(c for c in ''.join(g_1[i]))
    s = list(set(c) for c in g_2[i])
    g_2[i] = set.intersection(*s)

print(sum(len(g) for g in g_1))
print(sum(len(g) for g in g_2))
