s = input("Enter a sentence : ")
u=w=d=l=0
length = s.split()
w = len(length)
for c in s :
    if c.isdigit():
        d+=1
    elif c.isupper():
        u+=1
    elif c.islower():
        l+=1
print("No of words : ",w)
print("Words : ",length)
print("NO of Upper case characters : ",u)
print("No of Lower case characters : ",l)
print("No of Digits : ",d)