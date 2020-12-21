from math import prod

# Part 1
def two_elements_sum(list_of_nums, return_sum):
    '''Takes a list of numbers checks if any two numbers sum to the given sum returns -1 if no such pair exists'''

    for i, v1 in enumerate(list_of_nums, 1):
        for v2 in list_of_nums[i:]:
            if v1 + v2 == return_sum:
                return v1, v2

    return -1


with open("ExpenseReport.txt") as expense_report:
    print(prod(two_elements_sum([int(i) for i in expense_report.read().split()], 2020)))
    # Part 1: 1006875


# Part 2
def three_elements_sum(list_of_nums, return_sum):
    '''Takes a list of numbers checks if any three numbers sum to the given sum returns -1 if no such triplet exists'''

    for i, v1 in enumerate(list_of_nums, 1):
        for j, v2 in enumerate(list_of_nums[i:], i + 1):
            for v3 in list_of_nums[j:]:
                if sum((v1, v2, v3)) == return_sum:
                   return v1, v2, v3

    return -1


with open("ExpenseReport.txt") as expense_report:
    print(prod(three_elements_sum([int(i) for i in expense_report.read().split()], 2020)))
    # Part 2: 165026160
