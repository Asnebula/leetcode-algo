class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            # 如果s[i]这个字符出现过，并且当前起始字符的位置<=s[i]的位置(1-indexed)
            # 那么把起始字符的位置移动到s[i]这个字符的序号处(1-indexed)
            if s[i] in usedChar and start <= usedChar[s[i]]:  # @1这里很有探究意义的一点是为什么需要有“=”？
                start = usedChar[s[i]] + 1
            else:
                # 否则的话，maxlength就随着i的增加而+1，之后与之前的maxlength取较大值
                maxLength = max(maxLength, i - start + 1)
            # 保存“字符-序号”的键值对
            usedChar[s[i]] = i

        return maxLength
        # @1 因为userdChar是0-indexed，start是 1-indexed，二者相等，说明该usedChar已经比start位置上靠后一个了
        #   需要调整新的start
