class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        a = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        a.append(list(nums1_set - nums2_set))
        a.append(list(nums2_set - nums1_set))
        return a


sol = Solution()


nums1 = [1,2,3]
nums2 = [2,4,6]
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
# print(sol.findDifference(nums1, nums2))

set_1 = set(nums1)
set_2 = set(nums2)

print(set_1 - set_2)