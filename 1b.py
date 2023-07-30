num = int(input("Enter a interger : "))
string = str(num)
if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is Not a Palindrome")
for i in range(10):
    if string.count(str(i))>0:
        print(str(i),"Appears",string.count(str(i)),"Times")