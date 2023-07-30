m1 = int(input("Enter marks of Test 1: "))
m2 = int(input("Enter marks of Test 2: "))
m3 = int(input("Enter marks of Test 3: "))
if m1<=m2 and m1<=m3:
    avg = (m2+m3)/2
elif m2<=m1 and m2<=m3:
    avg = (m1+m3)/2
else:
    avg = (m1+m2)/2
print("The best of 2 tests are : ",avg)