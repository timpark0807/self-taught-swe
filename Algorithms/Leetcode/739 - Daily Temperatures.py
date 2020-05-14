class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(T)
        stack = []

        for index, temp in enumerate(T):
            while stack and temp > stack[-1][0]:
                answer[stack[-1][1]] = index - stack[-1][1]
                stack.pop() 
            stack.append((temp, index)) 

        return answer
