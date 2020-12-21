def password_length_match(policy, pword):
    len_range, letter = policy.split()
    return pword.count(letter) in range(int(len_range.split('-')[0]), int(len_range.split('-')[1]) + 1)


def password_pos_match(policy, pword):
    pos, letter = policy.split()
    return (pword[int(pos.split('-')[0]) - 1] == letter) ^ (pword[int(pos.split('-')[1]) - 1] == letter)


with open('PasswordCheck') as password_txt:
    pw = password_txt.read().splitlines()

cnt1 = 0
cnt2 = 0
for p in pw:
    cnt1 += int(password_length_match(*p.split(': ')))
    cnt2 += int(password_pos_match(*p.split(': ')))

print(cnt1)  # Part 1: 447
print(cnt2)  # Part 2: 249
