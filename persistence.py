#codewars.com 
#problem 2
#bekmuxtorov

def persistence(n: int) -> int:
    result = int()
    while True:
        if n < 10:
            return result
        numbers = [int(x) for x in str(n)]
        result += 1 
        n = 1
        for number in numbers:
            n *= number

print(persistence(39))

#<========================================> 😎Bajarildi <========================================>