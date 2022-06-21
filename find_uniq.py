#codewars.com 
#problem 22
#bekmuxtorov
#find_uniq

def find_uniq(arr):       
    for _ in range(len(arr)-1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            
    if arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]:
        n = arr[0]
        
    else:
        n = arr[len(arr)-1]
        
    return n
    
    
    
arr = [1, 1, 1, 0, 1, 1]
print(find_uniq(arr))