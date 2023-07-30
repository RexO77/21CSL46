def btod(bin):
    print("Given Binary Value: 0b",bin)
    decimal,i=0,0
    while(bin!=0):
        dec = bin%10
        decimal = decimal+dec*pow(2,i)
        bin//=10
        i+=1
    print("Decimal Value : ",decimal)
btod(1011)
def octToHex(n):
    print("Octel=",n)
    decnum = int(n,8)
    hexa = hex(decnum).replace("0x","")
    print("Hexadecimal value = ",hexa)
octToHex('5123')