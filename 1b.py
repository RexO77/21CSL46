str1 = input("Enter the String : ")    #reuced to 8 lines
if str1 == str1[::-1]:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
for i in range(10):
    if str1.count(str(i))>0:
        print(str(i),"appears",str1.count(str(i)),"Times")
