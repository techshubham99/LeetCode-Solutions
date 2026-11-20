class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """


        n = len(arr)
        zeros  = arr.count(0)

        for i in range(n-1,-1,-1):

            current = arr[i]

            if i+zeros < n:
                arr[i + zeros] = current

            if current == 0:
                zeros -=1


                if i + zeros < n:
                    arr[i + zeros] = 0



        