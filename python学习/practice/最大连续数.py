def max_sum(nums):
    max_sum,all_sum = 0,0
    for num in nums:
        all_sum = max(all_sum + num, num)# 当前数与之前的连续数总和 ，从正的开始
        max_sum = max(all_sum, max_sum) #可用的 和  与 之前最大的 比较
    return max_sum
print(max_sum([-2,1,-3,4,-1,2,1,-5,4])) 
print(max_sum([-2,1,-3,4,-1,2,1,-5,6])) 
