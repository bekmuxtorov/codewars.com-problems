#codewars.com 
#problem 20
#bekmuxtorov
#zeros
#Write a program that will calculate the number of trailing zeros in a factorial of a given number.

def zeros(n):
    s = 0
    while True:
        if n < 5:
            break
        else:
            s += n // 5
            n /= 5
            
    return int(s)

n=100
print(zeros(n))
        