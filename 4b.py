def romToDec(romstr):
    romdict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'K' : 1000
    }
    romback = romstr[::-1]
    val =0
    rval = romdict[romback[0]]
    for numaral in romback:
        lval = romdict[numaral]
        if lval<rval:
            val -= lval
        else:
            val += lval
    rval = lval
    return val
n = input("Enter a Roman Value : ")
print("Decimal Value is : ",romToDec(n))