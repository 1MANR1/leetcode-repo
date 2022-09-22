class Solution(object):
    def isValid(self, s):
        
        self.s = s
        self.list = []
        self.index = ''
        self.i = ''
        self.j = ''
        active = True
        self.place_holder = ''
        self.answers = []
        self.answer = ''
        

        for self.index in self.s:
            self.list.append(self.index)

        print(self.list)

        while active:
            for self.i in self.list:
                self.place_holder = self.i
                
                if self.place_holder == '(':

                    for self.j in self.list:

                        if self.j == ')':
                            self.answers.append('True') 
                            break
                    else:
                            self.answers.append('False')
                elif self.place_holder == ')':

                    for self.j in self.list:

                        if self.j == '(':
                            self.answers.append('True')
                            break
                    else:
                        self.answers.append('False')
                elif self.place_holder == '[': 

                    for self.j in self.list:

                        if self.j == ']':
                            self.answers.append('True')
                            break
                    else:
                        self.answers.append('False')            
                elif self.place_holder == ']':  

                    for self.j in self.list:

                        if self.j == '[':
                            self.answers.append('True')
                            break
                    else:
                        self.answers.append('False') 
                elif self.place_holder == '{':  

                    for self.j in self.list:

                        if self.j == '}':
                            self.answers.append('True')
                            break
                    else:
                        self.answers.append('False') 
                elif self.place_holder == '}': 

                    for self.j in self.list:

                        if self.j == '{':
                            self.answers.append('True')
                            break
                    else:
                        self.answers.append('False') 
                else:
                    self.answers.append('False')
                    active = False    
            else:
                active = False

        for self.answer in self.answers:
            if self.answer != 'True':
                return False

        return True


my_test = Solution()
print(my_test.isValid('[()'))


