from collections import Counter

# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:
#         length = len(grid)
        
#         rows = [tuple(row) for row in grid]
#         columns = [tuple(row[i] for row in grid) for i in range(length)]
        
#         counter = Counter(columns)
#         result = 0
#         for row in rows:
#             result += counter[row]
        
#         return result

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        dct = {}
        
        for row in grid:
            dct[tuple(row)] = dct.get(tuple(row), 0) + 1
        result = 0
        for col in zip(*grid):
            result += dct.get(tuple(col), 0)
        return result
        
        
grid = [
        [3,2,1],
        [1,7,6],
        [2,7,7]
        ]

grid = [
        [3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]
        ]

sol = Solution()

print(sol.equalPairs(grid))


