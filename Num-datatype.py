# NUMERIC DATATYPE
# Int 
# float 
# complex 

#INT

x=10;
y=3648200;
print(type(x));#<class 'int'>
print(type(y));#<class 'int'>

# Int is an whole num it contain an positive and negative value

z=-1678
print(type(z)); #<class 'int'>

# FLOAT
# float is also an contain an positve an negative value in points

a=1.56
b=-490.57
print(type(a)) # <class float>
print(type(b)) # <class float>

#float also contain a scientific num e power of 10

c=14.4e13
print(type(c))

# Complex
# complex nun is written with a 'j'

d=5j
e=2+2j
f=-4j
print(type(d)) # <class 'complex'>
print(type(e)) # <class 'complex'>
print(type(f)) # <class 'complex'>

# Type-Conversion

j=10; #int 
k=2.0 #float 
l=5j  #complex

# Convert  int j to float 
m=float(j)
print(m) # 10.0
print(type(m)) # <class 'float'>

# convert float k to complex
n=complex(k)
print(n) # 2+0j
print(type(n)) # <class 'complex'>


