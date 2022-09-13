class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        self.my_string = str(self.x)
        self.list = []
        self.add = ''
        self.reverse_list =[]
        
        for num in self.my_string:
            self.list.append(num)
        
        self.reverse_list = self.list[::-1]
            
        if self.list == self.reverse_list:
            return True
        else:
            return False
        

my_test = Solution()
print(my_test.isPalindrome(121))

