def twoSum(nums, target):
    sum = 0
    i = 0
    sum_digets = []
    active = True
    while active:
        range_list = len(nums) - 1
        for i in range(range_list):
            sum = nums[i] + nums[i+1]
            if (sum == target):
                sum_digets.append(i)
                sum_digets.append(i+1)
                active = False
            else:
                sum = nums[i+1]
                list_dialects = []

    return sum_digets


test_1 = twoSum([2, 7, 11, 15], 18)
print(test_1)
                 
        


    
        
