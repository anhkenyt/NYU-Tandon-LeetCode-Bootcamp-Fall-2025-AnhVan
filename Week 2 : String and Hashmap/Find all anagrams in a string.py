from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: List[int]
            """
        
        
            len_p = len(p)
            len_s = len(s)
            if len_p > len_s:
                return []

            count_p = Counter(p)
            window = Counter(s[:len_p])
            result = []

            if window == count_p:
                result.append(0)

            for i in range(len_p, len_s):
                start_char = s[i - len_p]
                new_char = s[i]
                window[new_char] += 1
                window[start_char] -= 1
                if window[start_char] == 0:
                    del window[start_char]

                if window == count_p:
                    result.append(i - len_p + 1)

            return result



if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"  
    solution = Solution()
    result = solution.findAnagrams(s,p)
    print(result)
    