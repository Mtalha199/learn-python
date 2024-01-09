# BOOLEAN
# boolean represent one of two values:True and False

print(10>9) # True
print(10<5) # False
print(100==99) # False

# Also run in if else statment 

x=4
y=7;
if x>y:
    print("x is greater")
else:
    print("y is greater")

# Bool() function
# Almost any value is evaluated to True if it has some sort of content.

print(bool("hello"))
print(bool(123))
print(bool(['apple','banana','orange']))

#Some values are false 

print(bool(None))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))
print(bool(False))