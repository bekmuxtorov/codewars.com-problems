#codewars.com 
#problem 15
#bekmuxtorov
#tocamelcase

def top_3_words(a):
    a_items = list(a.split(" "))
    counts = {}
    word_counts = []
    word_max_count = []
    max_word = []
    
    for i in range(len(a_items)-1):
        counts[ a.count(a_items[i])] = a_items[i]

    
    for word_count in counts:
        word_counts.append(word_count)

    
    for i in range(3):
        n = word_counts.index(max(word_counts))
        word_max_count.append(word_counts.pop(n))
        
    
    for i in range(len(word_max_count)):
        max_word.append(counts[word_max_count[i]])
        
    return max_word

a = "  //wont won't won't"

print(top_3_words(a))

    
