#python has no command line for variable

#CREATING VARIABLE
x=99;
y="TALHA";
print(x);
print(y);

#You can change type after set
a=99;
a='TALHA';
print(a);#TALHA

#Casting
#Also specify the datatype
b=str(1);  #'1'
c=int(1);  # 1
d=float(1) # 1.0

#Geting type
print(type(b)); #String
print(type(c)); #integer
print (type(d));#float

#Variable NAMES
#single Word
myvar="Talha";
my_var='Talha';
myVar='Talha';
MyVar="Talha";
MYVAR="Talha";
myVar2="Talha";

#Multi Words
#camelCase
myVariableName="Talha";

#PascalCase
MyVariableName="Talha";

#snake_case
my_variable_Name="Talha";

#printing Variable
#together
g,h,i='Orange','banana','apple';
print(g,h,i);

#Also by + operator
print(g+h+i);#print without spaces

#az a num it take + operoter for sum
j=3;
k=5;
print(j+k);#8

#python will give an error when you + for num and string
l=1;
m="talha";
# print(l+m);its better way to print is:
print(l,m);
