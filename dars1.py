"""<========================================> 1-masala <========================================>
def add_binary(a,b):
    bin_value = bin(a+b)
    return bin_value[2:]

print(f"{add_binary(1,1)}")
<========================================>😎Bajarildi <========================================>"""

#<========================================> 2-masala <========================================>
"""
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
"""
#<========================================> 😎Bajarildi <========================================>

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

# import math
# def find_next_square(sq):
#     sq_number = math.sqrt(sq)
    
#     if (sq_number).is_integer():
#         return int((sq_number+1)**2)
#     else: return -1
    
# sq = 225
# print(find_next_square(sq))


#<========================================>😎Bajarildi<========================================>


#<========================================> 12-masala <========================================>
"""Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""



#<========================================> 😏Tugatilmadi <========================================>"""

#<========================================> 13-masala <========================================>"""
"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched."""
"""
def pig_it(text: str) -> str:
    text_new_items = []
    text_items = list(text.split(" "))
    for text_item in text_items:
        new_item = text_item.insert(-1,text_item.pop(0))
        text_new_items.append(new_item)
    return text_items


print(pig_it("Pig latin is cool"))
"""
#<========================================> 😏Tugatilmadi <========================================>"""

#<========================================> 14-masala <========================================>"""
"""Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

"""
"""
#shaxsiy yechim
def count_bits(n: int) -> int:
    n_binary = bin(n)
    n_binary_i = n_binary[2:]
    n_binary_items = [int(x) for x in str(n_binary_i)]
    
    return n_binary_items.count(1)

print(count_bits(9))

#saytdagi yechim
def count_bits(n):
    return bin(n).count("1")

print(count_bits(9))

"""
#<========================================>😎Bajarildi<========================================>

#<========================================> 15-masala <========================================>"""
"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses 
is valid. The function should return true if the string is valid, and false if it's invalid.
"""
"""
def valid_parentheses(string: str) -> bool:
    counter = 0
    
    for character in string:
        if character == "(":
            counter += 1
            
        if character == ")":
            counter -= 1
            
        if counter < 0:
            return False
            
    return counter == 0



print(valid_parentheses("(()))("))
"""
#<========================================>😎Bajarildi<========================================>


#<========================================> 16-masala <========================================>"""
"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"""
"""
item_one : ()
item_two : []
item_tree : {}
"""
#shaxsiy yechim MUAMO: ketma-ket kelganlarini tanimayapti
"""
def valid_braces(string: str) -> bool:
    counter_item_one = 0
    counter_item_two = 0
    counter_item_tree= 0
    
    for character in string:
        if character == '(': counter_item_one += 1
        if character == ')': counter_item_one -= 1
        
        if character == '[': counter_item_two += 1
        if character == ']': counter_item_two -= 1


        if character == '{': counter_item_tree += 1
        if character == '}': counter_item_tree -= 1            
    
        if counter_item_one < 0: return False
        if counter_item_two < 0: return False
        if counter_item_tree < 0: return False
        
    return ((counter_item_one == 0) and (counter_item_two == 0) and (counter_item_tree == 0))
"""
#saytdagi yechim
# def valid_braces(string: str) -> bool:
#     simvols = []
#     all_simvols = {"{":"}","[":"]","(":")","}":"{","[":"]",")":"("}
#     for string_item in string:
#         if string_item == "(" or string_item == "[" or string_item == "{":
#             simvols.append(string_item)
#         else:
#             if len(simvols) == 0:
#                 return False
#             elif all_simvols[string_item] == simvols[len(simvols) - 1]:
#                 del simvols[len(simvols) - 1]
            
#             else:
#                 return False
            
#     if len(simvols) != 0:
#         return False
    
#     return True


# def validBraces(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0

#<========================================>😎Bajarildi<========================================>

#<========================================> 17-masala <========================================>
"""
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the
power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""

#shaxsiy yechim
"""
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

#saytdagi yechim:
def narcissistic(value):
    return value == sum(int(x)**len(str(value)) for x in len(value))
"""
#<========================================> 18-masala <========================================>
"""
Bola baland binoning n-qavatida to'p bilan o'ynamoqda. Bu qavatning balandligi h ma'lum.

U to'pni derazadan tashlab yuboradi. To'p o'z balandligining uchdan ikki qismiga (masalan, 0,66) sakraydi.

Onasi yerdan 1,5 metr naridagi derazadan tashqariga qaraydi.

Ona to'pning deraza oldidan o'tishini necha marta ko'radi (shu jumladan u yiqilib, sakrab tushayotganda?

To'g'ri tajriba uchun uchta shart bajarilishi kerak:
Float parametri "h" metrda 0 dan katta bo'lishi kerak
Float parametri "bounce" 0 dan katta va 1 dan kichik bo'lishi kerak
Float parametri "oyna" h dan kichik bo'lishi kerak.
Agar yuqoridagi uchta shart bajarilsa, ijobiy butun sonni qaytaring, aks holda -1 ni qaytaring.
"""
"""
def bouncing_ball(h,window, bounce = 2/3):
    if h > 0 and 0< bounce < 1 and window < h:
        heights = []
        while True:
            if h*bounce < window:
                return False
            heights.append(h*bounce)

        
        
    
    else:
        return -1     
print(bouncing_ball(81,1.5))    
"""
"""
import random
one = True * True #return 1
zero = True * False #rettrn 0
numbers = []

hundred = f"{one}{zero}{zero}"
for number in range(one, int(hundred)+1):
    numbers.append(number)
    
number_index = random.randint(one,int(hundred))
print(f"Kesib olingan son: {numbers[number_index]}")
numbers.pop(number_index)
print(numbers)    



words = input("Matnni kiriting: ")
print(words.split(" "))
print(len(words.split(" ")))
"""

#<========================================> 19-masala <========================================>
def domain_name(url):
    if url.index(".") == 10:
        begin = 11
        end = url.rindex(".")

    elif url.index(".") == 3:
        begin = 4
        end = url.rindex(".")
       
    elif url.index("/") == 5:
        begin = url.index("/") + 2
        end =   url.index(".")
        
    return url[begin:end]

url1 = "http://google.co.jp"
url2 = "www.xakep.ru"
url3 = "http://www.zombie-bites.com"
print(domain_name(url1))














































