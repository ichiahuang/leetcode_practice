# 001 two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        給定一個整數陣列 nums 和一個目標值 target，
        回傳陣列中**兩個數字**的索引，使得它們相加等於 target。
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = []  # 用來存放結果的索引

        while True:  # 兩層迴圈，嘗試所有配對
            for i in range(len(nums)-1):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        result.append(i)
                        result.append(j)
                        return result  # 找到就直接回傳