class MaskAddition:

    def __init__(self, nums, preamble_length):
        self.preamble_length = preamble_length
        self.nums = nums

    def find_first_invalid(self):
        for i, val in enumerate(self.nums[self.preamble_length + 1:], self.preamble_length + 1):
            for j in self.nums[i - self.preamble_length: i]:
                if val - j in self.nums[i - self.preamble_length: i] and val != (j << 1):
                    break
            else:
                return val

    def crack(self):
        code = self.find_first_invalid()
        vals, s = self.nums[:2], sum(self.nums[:2])
        i = 2

        while s != code:
            # print(vals, s)
            if s < code:
                s += self.nums[i]
                vals.append(self.nums[i])
                i += 1
            if s > code:
                s -= vals[0]
                vals = vals[1:]

        return min(vals) + max(vals)


with open("MaskCode") as mc_txt:
    m_add = MaskAddition([int(i) for i in mc_txt.read().strip().split()], 25)

print(m_add.find_first_invalid())  # Part 1
print(m_add.crack())  # Part 2
