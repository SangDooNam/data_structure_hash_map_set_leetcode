class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dct = {}
        for i in arr:
            dct[i] = dct.get(i, 0) + 1
        
        lst = sorted(dct.values())
        
        if len(lst) == len(set(lst)):
            return True
        else:
            return False
        



sol = Solution()
arr = [1,2,2,1,1,3]
arr = [1,2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(sol.uniqueOccurrences(arr))


