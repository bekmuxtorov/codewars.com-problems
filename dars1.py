"""<========================================> 1-masala <========================================>
def add_binary(a,b):
    bin_value = bin(a+b)
    return bin_value[2:]

print(f"{add_binary(1,1)}")
<========================================>😎Bajarildi<========================================>"""

#<========================================> 2-masala <========================================>
"""
def persistence(n):
    n_sections = [int(x) for x in str(n)]
    s = 1
    for n_section in n_sections:
        s *= n_section
    return s

print(persistence(39))
"""
#<========================================> 😏Tugatilmadi <========================================>

"""<========================================> 3-masala <========================================>

def order(sentence):
    order_items = sentence.split(" ")
    for order_item in order_items:
        order_item.split(" ")
       
word = "is2 Thi1s T4est 3a"
print(order(word))
<========================================> 😏Tugatilmadi <========================================>"""


"""<========================================> 4-masala <========================================>
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

<========================================>😎Bajarildi<========================================>"""

    
"""<========================================> 5-masala <========================================>
#Sizga bir so'z beriladi. Sizning vazifangiz so'zning o'rta belgisini qaytarishdir. Agar so'zning uzunligi
#toq bo'lsa, o'rtadagi belgini qaytaring. Agar so'z uzunligi juft bo'lsa, o'rtadagi 2 ta belgini qaytaring

def get_middle(s):
    n = len(s)
    if n % 2 != 0:
        return (f"{s[n//2]}")
    
    else:
        return (f"{s[n//2-1]}{s[n//2]}")
    
s = "Aa"
print(get_middle(s))
<========================================>😎Bajarildi<========================================>"""



"""<========================================> 6-masala <========================================>
#“Like” tizimini Facebook va boshqa sahifalardan bilsangiz kerak. Odamlar blog yozuvlari, rasmlari yoki
#boshqa narsalarni "yoqtirishi" mumkin. Biz bunday element yonida ko'rsatilishi kerak bo'lgan matnni yaratmoqchimiz.

def likes(names):
    n = len(names)              
    if   n == 0: return f"no one likes this"
    
    elif n == 1: return f"{names[0]} likes this"
    
    elif n == 2: return f"{names[0]} and {names[1].title()} like this"
    
    elif n == 3: return f"{names[0]}, {names[1]} and {names[2]} like this"
    
    else: return f"{names[0]}, {names[1]} and {n-2} others like this"
    
names = ["asadbek", "bobur", "gani", "boltaboy","gishmat"]
print(likes(names))
<========================================>😎Bajarildi<========================================>"""


#<========================================> 7-masala <========================================>
"""
The goal of this exercise is to convert a string to a new string where each character in the new 
string is "(" if that character appears only once in the original string, or ")" if that character
appears more than once in the original string. Ignore capitalization when determining if a character 
is a duplicate.
def dublicate_encode(word):
    n = len(word)
    return f"{'('*n}"

word = "Asadbek"
print(dublicate_encode(word))
"""
#<========================================> 😏Tugatilmadi <========================================>"""


#<========================================> 8-masala <========================================>
"""PROBLEM:Berilgan qatordagi unlilar sonini (hisobini) qaytaring.
Bu Kata uchun a, e, i, o, u unlilari sifatida qaraymiz (lekin y emas).
Kirish qatori faqat kichik harflar va/yoki bo'shliqlardan iborat bo'ladi."""
"""
def get_count(sentence):
    sentence = sentence.lower()
    vowal_letters = ["a", "e", "i", "o", "u"]
    count = 0
    sentence_letters = [str(x) for x in str(sentence)]
    for sentence_letter in sentence_letters:
        for vowal_letter in vowal_letters:
            if sentence_letter == vowal_letter:
                count += 1 
    return count

word = "Asadbek"
print(get_count(word))
"""
#<========================================>😎Bajarildi<========================================>


#<========================================> 9-masala <========================================>
"""PROBLEM: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false."""
"""
def validate_pin(pin):
    n = len(pin)
    if n == 0:
        return False
    
    pin_items = [str(x) for x in str(pin)]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    
    for pin_item in pin_items:
        if (pin_item in numbers) and ((n == 4) or (n == 6)):
            return True
        
        else:
            return False
        
pin = "123-"
print(validate_pin(pin)) 
To'liq tugatilmadi'


# saytdan ko'chirildi
def validator_pin(pin):
    return len(pin) in (4,6) and pin.isdigit()

pin = "1234"
print(validator_pin(pin))

"""
#<========================================>😎Bajarildi<========================================>


#<========================================> 10-masala <========================================>
"""There is an array with some numbers. All numbers are equal except for one. Try to find it!"""
"""
def find_uniq(arr):
    arr_counts = {}
    keys = []
    for i in range(len(arr)):
        arr_counts[arr.count(arr[i])] = arr[i]
        keys.append(arr.count(arr[i]))

    return arr_counts[min(keys)] 
 
arr = [1,1,1,20,20]
print(find_uniq(arr))"""
#<========================================> 😏Tugatilmadi <========================================>"""


#<========================================> 11-masala <========================================>
"""You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
"""
"""
import math
def find_next_square(sq):
    sq_number = math.sqrt(sq)
    
    if (sq_number).is_integer():
        return int((sq_number+1)**2)
    else: return -1
    
sq = 225
print(find_next_square(sq))
"""
#<========================================>😎Bajarildi<========================================>


#<========================================> 12-masala <========================================>
"""Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""

    


















