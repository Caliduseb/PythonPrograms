while True:
    print("")
    x = int(input("x = "))
    for basis in range(1000):
        for exponent in range(100):
            if basis ** exponent == x and basis != x:
                print(str(basis) + " ^ " + str(exponent))
    print("")
