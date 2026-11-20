class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        seen = set()
        unique = set()

        for num  in nums:

            if num in seen:
                unique.discard(num)

            else:
                seen.add(num)
                unique.add(num)

        return sum(unique)


