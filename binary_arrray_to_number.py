#codewars.com 
#problem 18
#bekmuxtorov
#binary_array_to_number  
#Given an array of ones and zeroes, convert the equivalent binary value to an integer.

def binary_array_to_number(array):
    s = ''
    for array_item in array:
        s += str(array_item)
        
    return int(s,2)


array = [0,0,1,0]
print(binary_array_to_number(array))

