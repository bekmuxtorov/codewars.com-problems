"""
Berilgan qavslar to'g'ri yopilganligiga tekshiring.
Qavslar - (), {}, [].
Misol uchun:
  valid_brackets("()()") = True
  valid_brackets("{()[]}") = True
  valid_brackets("{(]}") = False
"""

def valid_brackets(s: str) -> bool:
    """
    Kodni bu yerda yozing.
    """
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0

    for character in s:
        if character == "(":
            counter_1 += 1
        
        if character == ")":
            counter_1 -= 1
        
        if counter_1 < 0:
            return False
        
        if character == "{":
            counter_2 += 1
        
        if character == "}":
            counter_2 -= 1
        
        if counter_2 < 0:
            return False
        
        if character == "[":
            counter_3 += 1
        
        if character == "]":
            counter_3 -= 1
        
        if counter_3 < 0:
            return False

    return counter_1 == 0 and counter_2 == 0 and counter_3 == 0

#<========================================>😎Bajarildi<========================================>