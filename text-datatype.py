# Text Datatype
# String

txt="my name is talha"
print(txt)

# You can write multipe line by using three qoutes
# Note:in the result, the line breaks are inserted at the same position as in the code.

txt="""hello,
My name is Talha,
from Mandibahauddin"""
print(txt);

# String are are Arrays

txt="coder"
print(txt[0])# c

txt="Talha";
print(len(txt))# 5 # String length

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt="the best thing in life are free"
print("free" in txt)# True

#to check not in string

txt="the best thing in life are free"
print("expensive"not in txt)# true

# SLicing String 

txt="hello world!"
print(txt[2:5])# llo #first enter index included but entered  last index not included
print(txt[-10:-7])# llo 
print(txt[:8])# Slice from the start
print(txt[2:])# slice to  the end

# Modifying String 

txt=" taLha";
print(txt.upper())# TALHA # UPPER Case
print(txt.lower())# talha # LOWER Case
print(txt.split("L"))#['ta','ha'] #split case
print(txt.strip())#taLha #remove whitespaces
print(txt.replace("t","a"))# aaLha #replace String

#Concate String

txt="Muhammad"
txt1="Talha"
print(txt+txt1) # concatenation string

#Format String
#As we know we dont combine string and num for that we use format 

age=22;
txt="my age is {} " #curly braces is must
print(txt.format(age))
