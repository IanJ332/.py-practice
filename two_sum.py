class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            sub_num = nums[num.index(num) + 1]
            if target - num in nums:
                return [nums.index(num), sub_num.index(target - num) + 1]
        return False