# leetcode-0409-Longest Palindrome
# from collection import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = defaultdict(int) # 建立字典可儲存字母
        result = 0 # 因為對稱的程式碼左右相同，我們可以檢查是否字母出現次數為偶數

        for i in s: # 用for迴圈跑過每一項s
            dict[i] += 1 # 統計各字母出現次數
            if dict[i] % 2 == 0: # 若字母數量是偶數
                result += 2 #  將結果加2
        
        for j in dict.values(): # 逐一檢查字典(字母 : 次數)中次數的值 
            if j % 2 == 1: # 若有出現奇數代表該字母可被放在對稱字母的正中央
                result += 1 # 因此結果數值+1
                break # 因為中央字母只需要一個，一旦找到就跳出迴圈
        
        return results