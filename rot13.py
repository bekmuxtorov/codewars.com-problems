#codewars.com 
#problem 23
#bekmuxtorov
#rot13

def rot13(message):
    s = ''
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    letter =  ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m',' ']
    for message_item in message:
        index = letters.index(message_item.lower())
        if message_item.istitle():
            s += letter[index].upper()
        else:
            s += letter[index]
        
    return s
        
message = "Nffnybzh nyrxhz dnyRfm lnkfuvzvfm"
print(rot13(message))