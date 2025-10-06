class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # numbers is already sorted 
        answers = []
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if (numbers [j] + numbers[i] == target ):
                    answers.append(i+1)
                    answers.append(j+1)
            break
        return answers
x = Solution()
y = x.twoSum([2,7,11,15], 9)
print(y)