class two_sum:
    """A simple attemt to sum two numbers in a list with a target."""
    def __init__(self, list, target):
        self.list = list
        self.target = target
        self.answer = []
        self.sum = 0
        self.i = 0
        self.my_range = len(self.list)
        self.k = 0
    
    def two_sum_fun(self):
        j = 1
        active = True
        while active:
            for self.i in range(len(self.list)):
                self.sum += self.list[self.i]
                for self.k in range(self.my_range):
                    self.sum += self.list[self.k]
                    if self.sum == self.target:
                        self.answer.append(self.k)
                        self.answer.append(self.i)
                        active = False
                        return self.answer
                    else:
                        self.sum = self.list[self.i]
                        j += 1
                        print(j)
                        if j > 10**4:
                            return "Cannot search more"
                else:
                    self.sum = 0        
                
                            
my_test = two_sum([2,7,11,15], 22)
print(my_test.two_sum_fun())


        


    