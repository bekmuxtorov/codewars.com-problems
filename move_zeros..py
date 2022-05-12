#codewars.com 
#problem 17
#bekmuxtorov
#move_digits  
#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    zero_indexs = []
    new_array =[]
    for i in range(len(array)):
        if array[i] == 0:
            zero_indexs.append(i)
        else:
            new_array.append(array[i])
            
    for i in range(len(zero_indexs)):
        new_array.append(0)
        
    return new_array
    
array = [1, 0,0,0, 1,0, 2, 0, 0,1,3]
print(move_zeros(array))

