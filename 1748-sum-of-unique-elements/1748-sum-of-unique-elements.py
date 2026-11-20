class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Calculate unique sum
        ans = 0

        for num, count in freq.items():
            if count == 1:
                ans += num
        return ans
