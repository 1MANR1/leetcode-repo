class Solution(object):
    def isValid(self, s):

        self.s = s
        self.parantheses = {'(': ')', '[': ']', '{': '}'}
        self.answers = []

        for k in self.parantheses:
            if k in self.s:
                if self.parantheses[k] in self.s:
                    self.answers.append('True')
                else:
                    self.answers.append('False')

        for answer in self.answers:
            if answer != 'True':
                return False
        else:
            return True

my_test = Solution()
print(my_test.isValid('])'))




