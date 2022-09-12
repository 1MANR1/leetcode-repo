class Solution:    
    def twoSum(self, list, target):
        self.list = list
        self.target = target
        self.answer = []
        self.sum = 0
        self.i = 0
        self.my_range = len(self.list) - 1
        self.k = 1
        j = 1
        active = True
        while active:
            for self.i in range(len(self.list)):
                self.sum += self.list[self.i]
                for self.k in range(self.my_range):
                        self.sum += self.list[self.k]
                        if self.sum == self.target:
                            if self.k != self.i:
                                self.answer.append(self.k)
                                self.answer.append(self.i)
                                active = False
                                return self.answer[::-1]
                        else:
                            self.sum = self.list[self.i]
                            j += 1
                else:
                    self.sum = 0      

        


    