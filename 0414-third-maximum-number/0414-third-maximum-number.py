class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        first = None
        second = None
        third = None

        for num in nums:
             # 1. ignore duplicate
             if num == first or num == second or num == third:
                continue

            # 2. First maximum update
             if first is None or num > first:
                third = second
                second = first
                first = num

            # 3. Second maximum update
             elif second is None or num > second:
                third = second 
                second = num


            # 4. Third maximum update
             elif third is None or num > third:
                third = num

        # Return third  max if available
        if third is not None:
            return third

        # otherwise return first
        return first
