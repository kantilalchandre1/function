print('--------fun args---------')
def addition(x,y):  
     print (x+y)
     return
x=15  
print(addition(x ,10))
print(addition(x,x))
y=20  
print(addition(x,y))

print('--------positional args---------')
def sum(a,b):  
        c=a+b  
        print (c)  
sum(10,20)  
#sum(20) 

print('--------default args---------')
def msg(Id,Name='Rama',Age=21):  
         print (Id)
         print (Name)  
         print (Age)
         return  
msg(Id=100,Name='Ravi',Age=20)  
msg(Id=101,Name='Ratan') 
msg(Id=102)

print('--------keyword args---------')
def msg(id,name):  
            print (id)
            print (name)  
            return  
msg(id=100,name='Raj')  
msg(name='Rahul',id=101)  


print('-----local var---------')
def msg():  
        a=10  
        print ("Value of a is",a) 
        return  
msg()  
#print (a) 

print('-----global var---------')
b=20  
def msg():  
       a=10  
       print ("Value of a is",a)
       print ("Value of b is",b)
       return      
msg()  
#print (a)
print (b)

print('---call by ref---')
def ref(list1): 
   list1.extend([23,89]) 
   print ("list inside the function: ",list1)
list1 = [12,67,90] 
print ("list before pass", list1)
ref(list1) 
print ("list outside the function", list1)

print('---call by val---')
def fun(a):
   a=a+4
   print ("Inside the function", a)
a= 10
fun(a)
print ("Outside the function", a)
