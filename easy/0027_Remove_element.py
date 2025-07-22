# leetcode-0027-Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0  # 設i指針由最左邊開始，而j指針由最右邊開始
        j = len(nums) - 1
        while i <= j:  # 判斷使i和j可以跑過所有的值
            if nums[i] == val: # 當i檢查到的值等於val
                nums[i], nums[j] = nums[j], nums[i] # 將索引i和j的值交換
                j = j - 1 # 並使 j - 1 讓j下次交換是還沒檢查的值(左邊)
            else:
                i = i + 1 # if nums[i] != val使 i + 1 檢查下一個值(右邊)
        return j + 1