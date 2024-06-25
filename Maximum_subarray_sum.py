def kadane_algorithm(arr):
    n = len(arr)
    curr_sum = 0
    max_sum = float("-inf")
    
    
    for i in range(n):
        
        curr_sum  += arr[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            
        if curr_sum < 0:
            curr_sum = 0
        
    return max_sum


# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [1,2,3]
ans = kadane_algorithm(arr)
print(ans)            