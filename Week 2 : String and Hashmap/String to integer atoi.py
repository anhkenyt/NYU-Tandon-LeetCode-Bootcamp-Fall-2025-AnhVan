class Solution(object):
    def myAtoi(self, s):
        # Hashmap for digits
        digits = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }

       
        s = s.lstrip()
        if not s:
            return 0

    
        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            i += 1

       
        num = 0
        while i < len(s) and s[i] in digits:
            num = num * 10 + digits[s[i]]
            i += 1

   
        num *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
if __name__ == "__main__":
    s = "42"
    solution = Solution()
    result = solution.myAtoi(s)
    print("Converted integer:", result)