from time import time

class Ticket:

    def __init__(self, ticket_nums):
        self.ticket_nums = ticket_nums

    def invalid_values(self, rule_vals):
        '''
        :param rule_vals: a combination of all possible values
        :return: all invalid values on a ticket, is empty if there are no invalid numbers
        '''
        i_v = []
        for ticket_num in self.ticket_nums:
            if ticket_num not in rule_vals:
                i_v.append(ticket_num)

        return i_v

    def possible_fields(self, rule):
        '''
        :param rule: a dict of rules
        :return: returns a list which sontains a set of all possible fields at a given position
        '''

        possible = []

        for num in self.ticket_nums:
            possible.append(set())
            for r in rule:
                if num in rule[r]:
                    possible[-1].add(r)

        return possible

    def __repr__(self):
        return 'Ticket(' + str(self.ticket_nums) + ')'


start = time()
with open("TrainRules") as tr_txt:
    rules_, my_ticket_, other_tickets_ = tr_txt.read().split('\n\n')  # text parsing


rules = {}
for r in rules_.splitlines():
    field, vals = r.split(':')

    vals = vals.strip().split(' or ')

    v_ = tuple(range(int(v.split('-')[0]), int(v.split('-')[1]) + 1) for v in vals)

    vals = set()

    for v in v_:
        vals |= set(v)

    rules[field] = vals  # parsing the rules section into a dictionary that contains all values


# Parsing nearby tickets into Ticket objects
other_tickets = [Ticket([int(i) for i in t.split(',')]) for t in other_tickets_.splitlines()[1:]]


# all possible values that indicate valid tickets
all_nums = set()
for r in rules:
    all_nums |= rules[r]


print(sum(sum(t.invalid_values(all_nums)) for t in other_tickets))  # part 1
print(time() - start)
print()

# removes all invalid tickets
valid_tickets = [t for t in other_tickets if not t.invalid_values(all_nums)]


# creates an initial list where a set of all possible fields on the ticket can be at any position
pos = [set(rules.keys()) for _ in range(len(rules))]


# for every ticket, intersect our initial list with the results of possible fields on valid tickets
for t in valid_tickets:
    possible = t.possible_fields(rules)
    pos = [pos[i] & possible[i] for i in range(len(pos))]


# parsing our ticket into a list
my_ticket = [int(i) for i in my_ticket_.splitlines()[1].split(',')]

# creating an empty dict to fill when we discover a field position
my_guided_ticket = {}

# if there is only one possible field at a position, it marks it on our ticket and removes it from all other positions
# would create infinite loop if there is no possible solution, but we can assume there is one
while any(p for p in pos):
    for i in range(len(pos)):
        if len(pos[i]) == 1:
            found = next(iter(pos[i]))
            my_guided_ticket[found] = my_ticket[i]

            for p in range(len(pos)):
                try:
                    pos[p].remove(found)
                except KeyError:
                    continue


d = 1

for r in my_guided_ticket:
    if r.startswith('depart'):
        d *= my_guided_ticket[r]

print(d)  # part 2
print(time() - start)
