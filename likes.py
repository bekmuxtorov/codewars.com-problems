#codewars.com 
#problem 5
#bekmuxtorov
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

#<========================================>😎Bajarildi<========================================>