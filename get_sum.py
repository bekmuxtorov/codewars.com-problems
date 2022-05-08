#codewars.com 
#problem 3
#bekmuxtorov

def get_sum(a,b):
    s = 0
    if a == b:
        return a
    
    elif a < b:
        for a_son in range(a,b+1):
            s +=a_son
        return s
    
    else:
        for a_son in range(b,a+1):
            s +=a_son
        return s

#<========================================>😎Bajarildi<========================================>