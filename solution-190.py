def maxCyclicSum(arr):  
    if len(arr)==0: 
        return 0
    sumN=max_sum=min_sum=current_sum_max=current_sum_min=arr[0]   
    for num in arr[1:]: 
        current_sum_min=min(current_sum_min+num, num)
        current_sum_max=max(current_sum_max+num, num)
        min_sum=min(current_sum_min, min_sum)
        max_sum=max(current_sum_max, max_sum)
        sumN +=num
    return max(max_sum,sumN-min_sum) if sumN-min_sum!=0 else max_sum

assert maxCyclicSum([8, -1, 3, 4])==15
assert maxCyclicSum([-4, 5, 1, 0])==6
