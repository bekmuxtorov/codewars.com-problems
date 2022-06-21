#codewars.com 
#problem 21
#bekmuxtorov
#is_isogram
#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.


def is_isogram(string):
    if string == "":
        return True
    else:
        string_items = [str(x) for x in str(string.lower())]
        string_new_items = [str(x) for x in set(string.lower())]
        
        return len(string_items) ==len(string_new_items) and string.isalpha()

string = "moOse"
print(is_isogram(string))

#<========================================>😎Bajarildi<========================================>