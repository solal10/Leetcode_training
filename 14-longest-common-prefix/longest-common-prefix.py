class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_pre=[]
        for i in range(len(strs[0])):
            common_pre.append(strs[0][i])
            for j in range(1,len(strs)):
                 if i >= len(strs[j]) or common_pre[i] != strs[j][i]:
                        common_pre.pop()
                        return ''.join(common_pre)
                        break
        return ''.join(common_pre)
