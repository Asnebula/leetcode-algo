class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]
        # return None

        # 只用了一层for loop
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


solu = Solution()
print(solu.twoSum([2, 0, 6, 15], 9))
