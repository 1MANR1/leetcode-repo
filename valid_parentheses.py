class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.s = s
        self.list = []
        self.i = ""
        self.j = 0
        self.answers = []
        self.asnwer = ''
        
        
        
        for self.i in self.s:
            self.list.append(self.i)
        
        
        
        while self.j < len(self.list):
                        
            if self.list[self.j] == "(" and self.list[self.j + 1] == ")":
                self.answers.append('True')
            elif self.list[self.j] == "[" and self.list[self.j + 1] == "]":
                self.answers.append('True')
            elif self.list[self.j] == "{" and self.list[self.j + 1] == "}":
                self.answers.append('True')
            else:
                self.answers.append('False')
            
            self.j += 2
              
        for self.answer in self.answers:
            if self.answer != 'True':
                return False
        
        
        return True
    
my_test = Solution()
print(my_test.isValid("{[]}"))