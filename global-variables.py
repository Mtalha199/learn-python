#GLOBAL VARIABLE DECLARATION
#we can access a variable in a function and also outside of function if we declare a variable in global 

x="TALHA";
def myfunc():
    print("My Name is "+x);#TALHA
myfunc()

#If create a variable in function with a same name global variable remain original 
y="Pakistan";

def my_function():
    y="zindabad";                  #Within a function it can be acces only in a function locally
    print("Inside a function:"+y); #zindbad
my_function()
print("Outside a function:"+y);#pakistan

#we can access a local varible as global by using global keyword

def MyFunction():
    global a
    a="mandi bahauddin";
MyFunction()
print("Outside but acces inside variable:"+a);#mandi bahauddin

#IF we change a value by same name within a function and outside 

z="ISLAMABAD";
def myFunction():
    global z
    z="LAHORE";
myFunction()
print(z);#LAHORE    