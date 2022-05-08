#codewars.com 
#problem 13
#bekmuxtorov
# You are given an array (which will have a length of at least 3, but could
# be very large) containing integers. The array is either entirely comprised
# of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns
# this "outlier" N.


def find_outlier(integers):
    if sum(integers) % 2 == 0:
        for integer in integers:
            if integer % 2 == 0:
                integers.remove(integer)
                return integer
    
    else:
        for integer in integers:
            if integer % 2 != 0:
                integers.remove(integer)
                return integer
    
a_sonlar = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(a_sonlar))
    
    
#<========================================>😎Bajarildi<========================================>