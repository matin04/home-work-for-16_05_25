str1=input()
str2=0
str3=0
for i in str1:
    if i.isupper():
        str2+=1
    elif i.islower():
        str3+=1
print(str2)
print(str3)