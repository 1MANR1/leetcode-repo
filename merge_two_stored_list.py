class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        self.list1 = list1
        self.list2 = list2
        self.asnwers = []
        if self.list1:
            for number1 in self.list1:
                self.asnwers.append(number1)
        if self.list2:
            for number2 in self.list2:
                self.asnwers.append(number2)
        
        self.asnwers.sort()
        return self.asnwers

my_test = Solution()
print(my_test.mergeTwoLists(list1 = [1 ,2, 4], list2 = [1, 3, 5]))
