def xor(o, t):
    if o == t:
        return '0'
    else:
        return '1'


while True:
    msg = input("msg > ").replace(" ", "_")
    key = input("key > ").replace(" ", "_")+str("a"*500)

    msgArray = []
    keyArray = []
    for char in list(msg):
        for bit in list("{0:b}".format(ord(char))):
            msgArray.append(bit)
    for char in list(key):
        for bit in list("{0:b}".format(ord(char))):
            keyArray.append(bit)

    enc = ''

    for index in range(msgArray.__len__()):
        enc += xor(msgArray[index], keyArray[index])

    print(enc)
    input("")
