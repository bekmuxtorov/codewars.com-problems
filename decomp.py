#codewars.com 
#problem 22
#bekmuxtorov
#decomp
def shellsort(array, n):
    temp = n//2
    while temp > 0:
        j = temp
        while j < n:
            i = j - temp
            while i >= 0:
                if array[i+temp] > array[i]:
                    break
                else:
                    array[i+temp], array[i] = array[i], array[i+temp]
                i = i - temp    
            j += 1
        temp = temp//2
    

a_sonlar = [12,5,87,23,64]
print(f"kiritilgan to'plam:{a_sonlar}")

shellsort(a_sonlar, len(a_sonlar))
print(f"tartiblangan to'plam:{a_sonlar}")
