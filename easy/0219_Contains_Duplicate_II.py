# leetcode-0219-Contains Duplicate II
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {} # 用字典紀錄index, value (value:index)
        for index, value in enumerate(nums): # 使用迴圈跑過nums中的每一個值
            if value in dict:
                if index - dict.get(value) <= k: # 判斷相同數字的距離是否 <= k
                    return True
                else:
                    dict[value] = index # 若相同數字的距離沒有 <= k，則更新dict中的key:value
            else:
                dict[value] = index # 若dict中沒有紀錄到value，則將此組key:value新增到dict
        return False # 若最後都沒有找到符合條件的距離，則return False