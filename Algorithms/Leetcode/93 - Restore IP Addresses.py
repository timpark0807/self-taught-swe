class Solution(object):
    def restoreIpAddresses(self, string):
        if len(string) < 4:
            return []
        answers = []
        self.backtrack(string, answers, [])
        for index, answer in enumerate(answers):
            answers[index] = ".".join(answer)
        return answers

    def backtrack(self, string, answers, curr):
        if not string and len(curr) == 4:
            answers.append(curr[::])

        if len(curr) == 4:
            return

        for index in range(len(string)):
            if self.is_valid(string[:index+1]):
                curr.append(string[:index+1])
                self.backtrack(string[index+1:], answers, curr)
                curr.pop()

    def is_valid(self, string):
        if len(string) > 1 and string[0] == '0':
            return False 
        return 0 <= int(string) <= 255  
