class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
    
    
        words = s.split()
    
        reversed_words = words[::-1]
       
        return ' '.join(reversed_words)

if __name__ == "__main__":
    s = "the sky is blue"
   
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)
    