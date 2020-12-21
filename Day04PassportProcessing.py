import re


pp_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
}


def valid_passport(passport):

    try:
        hgt_cm = passport['hgt'][-2:] == 'cm'

        return all((
            any(passport.keys() == pp_f for pp_f in (pp_fields, pp_fields - {'cid'})),
            int(passport['byr']) in range(1920, 2003),
            int(passport['iyr']) in range(2010, 2021),
            int(passport['eyr']) in range(2020, 2031),
            int(passport['hgt'][:-2]) in (range(150, 194) if hgt_cm else range(59, 77)),
            re.match(r'^#[\da-f]{6}$', passport['hcl']),
            passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
            re.match(r'^\d{9}$', passport['pid']),
        ))
    except KeyError:
        return False
    except ValueError:
        return False


with open("PassportBatch") as pb_txt:
    passports = [pp.strip().split() for pp in pb_txt.read().split('\n\n')]

cnt = 0

for pp in passports:
    cnt += int(valid_passport({pair.split(':')[0]: pair.split(':')[1] for pair in pp}))

print(cnt)
