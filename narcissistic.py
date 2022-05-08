#codewars.com 
#problem 11
#bekmuxtorov
# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the
# power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

def narcissistic(value: int) -> bool:
    value = str(value)
    value_new_items = []
    s = 0
    
    value_items = [int(x) for x in str(value)]
    n = len(value)
    for value_item in value_items:
        value_new_items.append(value_item**n)
    
    
    for value_new_item in value_new_items:
        s += value_new_item
        
    s = str(s)
        
    return value == s

print(narcissistic(153))

#<========================================>😎Bajarildi<========================================>
#saytdagi yechim
# def narcissistic(value):
#     return value == sum(int(x)**len(str(value)) for x in len(value))
