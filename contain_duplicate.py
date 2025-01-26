class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = []
        for num in nums:
            if num in hash_set:
                return True
            hash_set.append(num)
        return False