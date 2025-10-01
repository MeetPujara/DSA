class Solution:
    def reverse(self, arr: list, start: int, end: int) -> None:
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        self.reverse(arr, start+1, end-1)


sol = Solution()
lst = [1, 2, 3, 4, 5]
sol.reverse(lst, 0, len(lst)-1)
print(lst) 
