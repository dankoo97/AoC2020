bags = {}

with open('BagRules') as rules_txt:
    for rule in rules_txt.read().strip().split('\n'):

        big_bag = rule.split(' bags contain ')[0]
        small_bags = rule.split(' bags contain ')[1].strip('.')

        if small_bags == 'no other bags':
            bags[big_bag] = None
        else:
            bags[big_bag] = {small[2:].rstrip('s').replace(' bag', ''): int(small[:1]) for small in small_bags.split(', ')}


def how_many_bags(goal_bag):
    bag_colors = set()
    for bag in bags:
        if bags[bag] and goal_bag in bags[bag]:
            bag_colors.add(bag)
            bag_colors |= how_many_bags(bag)

    return bag_colors


def nesting_bags(start):
    if not bags[start]:
        return 0

    cnt = 0

    for bag in bags[start]:
        cnt += bags[start][bag] * (1 + nesting_bags(bag))

    return cnt


print(len(how_many_bags('shiny gold')))
print(nesting_bags('shiny gold'))
