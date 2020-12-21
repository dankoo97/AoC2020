import math


class Adapters:

    def __init__(self, adapter_list):
        self.adapter_list = [0] + adapter_list
        self.adapter_list.sort()
        self.adapter_list.append(self.adapter_list[-1] + 3)

    def sol_1(self):
        cnt1, cnt3 = 0, 0
        for adapter in self.adapter_list:
            if adapter + 1 in self.adapter_list:
                cnt1 += 1
            elif adapter + 3 in self.adapter_list:
                cnt3 += 1

        return cnt1, cnt3

    def sol_2(self):
        sol_vector = []

        for i in range(len(self.adapter_list) - 3):
            sol_vector.append(len({self.adapter_list[i] + j for j in (1, 2, 3)} & {self.adapter_list[i + j] for j in (1, 2, 3)}))

        step_2 = ''.join(str(i) for i in sol_vector).split('1')

        step_3 = [sum(int(i) for i in s) for s in step_2 if s]

        step_4 = [s - 1 if s != 2 else 2 for s in step_3]

        return math.prod(step_4)


with open("JoltAdapters") as ja_txt:
    a = Adapters([int(i) for i in ja_txt.read().split()])

p = lambda x, y: x * y

print(p(*a.sol_1()))  # Part 1

print(a.sol_2())  # Part 2
