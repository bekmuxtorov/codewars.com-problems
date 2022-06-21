def merge_two_arrays(arr1, arr2):
    for arr2_item in arr2:
        arr1.added(arr2_item)
    return arr1.sort()
        
    

    
    
        
        
        
    
    
        
    
        
print(merge_two_arrays([4,5], [3]))
