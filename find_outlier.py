#codewars.com 
#problem 13
#bekmuxtorov
# You are given an array (which will have a length of at least 3, but could
# be very large) containing integers. The array is either entirely comprised
# of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns
# this "outlier" N.


def find_outlier(integers):
    juft_sonlar = [int(i) for i in integers if i % 2 == 0]
    toq_sonlar =  [int(i) for i in integers if i % 2 != 0]
    
    if len(juft_sonlar) == 1: return juft_sonlar[0] 
    else: return toq_sonlar[0] 
        
    
a_sonlar = [-3636911, -8199133, -8977659, 3921971, 962191, -7968639, -4730561, 4475859, -7468481, -5060519, 1353745, -2366563, 9614377, 4390555, 6902285, 6839969, -4032420, 8016157, -978645, 832613, 3388935, 6348791, -1942791, -946591, 9560607, -5722977, -3420395, 2382197, -2372683, 8117379, 4709395, 9647421, 7790849, -5078647, -4586801, 1428317, 496705, 6465085, 8974103, -1333711, -1826573, 8829957, -7829083, 198953, -9023749, 2531709, -2965057, 3234257, 4730639, -4124231]
print(find_outlier(a_sonlar))
    
    
#<========================================>😎Bajarildi<========================================>