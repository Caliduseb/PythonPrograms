def xor(o, t):
    if o == t:
        return '0'
    else:
        return '1'


while True:
    msg = input("crypt > ").replace(" ", "_").replace(",", " ")
    key = input("key > ").replace(" ", "_").replace(",", " ")

    keyArray = []
    for char in list(key):
        for bit in list("{0:b}".format(ord(char))):
            keyArray.append(bit)

    dec = ''
    cl = ''
    for index in range(list(msg).__len__()):
        dec += xor(list(msg)[index], keyArray[index])

    for charnum in range(int(dec.__len__()/7)):
        char = int(dec[7*charnum:7*charnum+7], 2)
        cl += str(chr(char))

    print(cl)
