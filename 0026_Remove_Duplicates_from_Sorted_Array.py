# leetcode-0026-Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1 # 設左指針從1開始
        for r in range(1,len(nums)):  # 右指針從1開始到最後一數字
            if nums[r] != nums[r - 1]:  # if右指針碰到的數字和前一個數字不同，則遇到新的數字
                nums[l] = nums[r]  # 將新數字指定給左指針的索引
                l = l + 1 # 記錄下l的次數
        return l
