numbers = ('2 4 7 8 10')
def iq_test(numbers):
    num = numbers.split()
    num1 = list(map(int,num))
    for x in num1:
        if x % 2 ==1:
            return num1.index(x) + 1
        
   
    
            
    



    #return print(num1)



print(iq_test(numbers))
