#codewars.com 
#problem 14
#bekmuxtorov
#You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
#Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

def diamond(n):
    if n < 0 or n % 2 ==0:
        return None

    else:
        s = ' '
        for i in range(1,n+1,2):
            print(f"{'*'*i}".center(n))

        for j in range(n-2,0,-2):
            print(f"{'*'*j}".center(n))
        return s 
        
print(diamond(5))