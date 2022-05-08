#codewars.com 
#problem 6
#bekmuxtorov
# Berilgan qatordagi unlilar sonini (hisobini) qaytaring.
# Bu Kata uchun a, e, i, o, u unlilari sifatida qaraymiz (lekin y emas).
# Kirish qatori faqat kichik harflar va/yoki bo'shliqlardan iborat bo'ladi.

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