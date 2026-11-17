class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)

        if n<3:
            return False

        i =0

        #increase
        while i+1 < n and arr[i] < arr[i+1]:
            i+=1
        
        #peak starting or ending point nahi hona chyie
        if i==0 or i==n-1:
            return False

        #decreasing part
        while i+1 < n and arr[i] > arr[i+1]:
            i+=1

        return i==n-1