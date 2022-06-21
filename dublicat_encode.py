#codewars.com 
#problem 21
#bekmuxtorov
#dublicate_encode
#The goal of this exercise is to convert a string to a new string where 
#each character in the new string is "(" if that character appears only 
#once in the original string, or ")" if that character appears more than
#once in the original string. Ignore capitalization when determining if 
#a character is a duplicate.

def duplicate_encode(word :str) -> str:
    s = 1
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            if word[i] == word[j]:
                s += 1
    return s

word = "idinii"
print(duplicate_encode(word))
    
