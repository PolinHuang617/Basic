#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力法
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target - nums[j] == nums[i]:
        #             return i, j
        # return 0

        # 2. 字典
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], index]
            dict[num] = index
        # print(dict)
# @lc code=end

