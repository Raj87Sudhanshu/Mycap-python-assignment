nterms = int(input ("How many terms you wants to print: "))  
 
n1 = 0  
n2 = 1  
count = 0  
  
if nterms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
elif nterms == 1:  
    print ("The Fibonacci sequence of the numbers up to", nterms, ": ")  
    print(n1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < nterms:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count += 1 
        
#input = How many terms you wants to print: 5
#output = The fibonacci sequence of the numbers is:
#         0
#         1
#         1
#         2
#         3
