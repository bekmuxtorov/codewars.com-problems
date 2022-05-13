#codewars.com 
#problem 19
#bekmuxtorov
#

# def aniqla(son):
#     s = ''
#     frend_1=[1,2,4]
#     frend_2=[1,2,3,5]
#     frend_3=[2,3,6]
#     frend_4=[1,4,5,7]
#     frend_5=[2,4,5,6,8]
#     frend_6=[3,5,6,9]
#     frend_7=[4,7,8]
#     frend_8=[5,7,8,9]
#     frend_9=[6,8,9]
#     frend_0=[0,8]
    
#     frend = [frend_0, frend_1, frend_2, frend_3, frend_4, frend_5, frend_6, frend_7, frend_8, frend_9]
    
#     son_items = [int(x) for x in str(son)]
    
#     for i in frend[son_items[0]]:
#         for j in frend[son_items[1]]:
#             s += f"{i}{j},"
    
#     s= s

# son = 22
# print(aniqla(son))


def last_digit(n1,n2):
    last_number_n1 = [int(x) for x in str(n1)][-1]
    
    if [int(x) for x in str(n2)][-1] == 0 and last_number_n1 == 0: return  0 
    elif [int(x) for x in str(n2)][-1] == 0: return 1
    else:
    #Faqat bir xil sin bilan tugaydigonlar
    if last_number_n1 == 0: s= 0
    if last_number_n1 == 1: s= 1
    if last_number_n1 == 5: s= 5
    if last_number_n1 == 6: s= 6
    
    
    #Faqat ikki xil son bilan tugaydigonlar
    if last_number_n1 == 4:
        if n2 % 2 == 0: s= 6
        else: s= 4
        
    if last_number_n1 == 9:
        if n2 % 2 == 0: s= 1
        else: s= 9
        
        
    #Faqat to'rt xil raqam bilan tugaydigonlar
    if last_number_n1 == 2:
        if n2 % 4 == 1: s= 2
        if n2 % 4 == 2: s= 4
        if n2 % 4 == 3: s= 8
        if n2 % 4 == 0: s= 6
            
    if last_number_n1 == 3:
        if n2 % 4 == 1: s= 3
        if n2 % 4 == 2: s= 9
        if n2 % 4 == 3: s= 7
        if n2 % 4 == 0: s= 1      
        
    if last_number_n1 == 7:
        if n2 % 4 == 1: s= 7
        if n2 % 4 == 2: s= 9
        if n2 % 4 == 3: s= 3
        if n2 % 4 == 0: s= 1
            
    if last_number_n1 == 8:
        if n2 % 4 == 1: s= 8
        if n2 % 4 == 2: s= 4
        if n2 % 4 == 3: s= 2
        if n2 % 4 == 0: s= 6
        
    
    
    return s

n1, n2 = 10, 10 ** 10
print(last_digit(n1, n2)) 
    
        






































