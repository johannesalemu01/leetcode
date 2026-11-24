class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_arr = []
            for i in range(0, len(s), k):
                new_arr.append(s[i : i + k])

            next_s = []
            for total in new_arr:
                digit_sum = sum(int(c) for c in total)
                next_s.append(str(digit_sum))

            s = "".join(next_s)

        return s