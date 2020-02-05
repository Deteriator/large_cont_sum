'''
P: Given an array find the largest continuous sum

E:
large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) == 29
large_cont_sum([1,2,-1,3,4,-1]) == 9
large_cont_sum([-1,1]) == 1

D: List, dictionary, integer


A: Given an array 
    loop over array and gather both a current max and running maximum
        curr_max from the current index number and the current + the index number
        max_sum from the current max and the overall max
    return max_sum
    

'''
def large_cont_sum(arr):
    max_sum = arr[0] 
    curr_max = arr[0] 
      
    for i in range(1,len(arr)): 
        curr_max = max(arr[i], curr_max + arr[i]) 
        max_sum = max(max_sum,curr_max) 
          
    return max_sum
    
print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
print(large_cont_sum([1,2,-1,3,4,-1]))
print(large_cont_sum([-1,1]))
print(large_cont_sum([-100,-10,-1,-3,-2]))
print(large_cont_sum([-10, 2,-1, 30, 4,-100,-10,-10,17]))


def large_cont_sum2(arr): 
    curr_max = 0
    max_sum = 0
      
    for i in range(0, len(arr)): 
        max_sum = max_sum + arr[i] 
        if max_sum < 0: 
            max_sum = 0
        elif (curr_max < max_sum): 
            curr_max = max_sum
              
    return curr_max
print(large_cont_sum2([1,2,-1,3,4,10,10,-10,-1]))