Coins = {2.00: "2eur", 1: "1eur",0.50: "50ct", 0.20: "20ct", 0.10: "10ct", 0.05: "5ct", 0.02: "2ct", 0.01: "1ct"}
preis = float(input("rückgeld: "))
imSinn = preis + 0.00001
change = []
for i in Coins:
    while imSinn > i:
        change.append(Coins[i])
        imSinn -= i

print(change)
