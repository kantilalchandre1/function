print('---------sum function-----')
def sum(x,y):  
          s=x+y  
          print ("Sum of two numbers is" ,s)
sum(10,20) 
sum(20,30)  

print('---------sum function with return stmt-----')
def sum1(a,b):  
            print ("Printing within Function")
            print (a+b)  
            return a+b  
def msg():  
            print ("Hello")
            return  
      
total=sum1(10,20)  
print ("Printing Outside",total)
msg()  
print ("Rest of code")  
