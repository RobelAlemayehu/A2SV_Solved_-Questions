class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""


        if len(strs) == 1:
            return strs[0]

        common = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != ch:
                    return common 
            common += ch 
        return common
        
 
             
