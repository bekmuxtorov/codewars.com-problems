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
#<========================================>😎Bajarildi<========================================>




























