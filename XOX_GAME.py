a = ["E", "E", "E"]
b = ["E", "E", "E"]
c = ["E", "E", "E"]
d = ["XXX", "OOO"]


def horizontal_line(a):
    b = "".join(a)
    if any(i in b for i in d):
        if d[0] in b:
            print("******X****** GEWONNEN (horizantal)")
            return True
        elif d[1] in b:
            print("*****O****** GEWONNEN (horizantal) ")
            return True


def vertical_line(a, b, c):
    ''' bu bir doctur
    '''
    ver = list(map(lambda x, y, z: x + y + z, a, b, c))
    if any(i in ver for i in d):
        if d[0] in ver:
            print("******X****** GEWONNEN (vertical) ")
            return True
        elif d[1] in ver:
            print("*****O****** GEWONNEN (vertical)")
            return True


def kreuz(a, b, c):
    if a[0] == b[1] == c[2] or a[2] == b[1] == c[0]:
        if (a[0] == "X" and b[1] != "E") or (a[2] == "X" and b[1] != "E"):
            print("******X****** GEWONNEN (kreuz)")
            return True
        elif (a[0] == "O" and b[1] != "E") or (a[2] == "O" and b[1] != "E"):
            print("*****O****** GEWONNEN (kreuz)")
            return True


def kontrol(a, b, c):
    if bool(vertical_line(a, b, c)) or bool(horizontal_line(a)) or bool(horizontal_line(b)) or bool(horizontal_line(c)) or bool(kreuz(a, b, c)):
        return True


countx = 0
conto = 1
i = 0
while i < 10 and kontrol(a, b, c) != True:
    i += 1

    if conto > countx:
        countx += 1

        x = input(
            "x bitte ihre komb. eingegeben erste Zeile nach Spalte Z.B: 12 ===>>   ").upper()

        if int(x[0]) == 1:
            if a[int(x[1])-1] == "E":
                a[int(x[1])-1] = "X"
                print(a, b, c, sep="\n")

            else:
                x = input(
                    "x bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12===>>   ").upper()
        elif int(x[0]) == 2:
            if b[int(x[1])-1] == "E":
                b[int(x[1])-1] = "X"
                print(a, b, c, sep="\n")

            else:
                x = input(
                    "x bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12===>>   ").upper()

        elif int(x[0]) == 3:
            if c[int(x[1])-1] == "E":
                c[int(x[1])-1] = "X"
                print(a, b, c, sep="\n")

            else:
                x = input(
                    "x bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12===>>   ").upper()

    else:
        conto += 1
        o = input(
            "o bitte ihre komb. eingegeben  erste Zeile nach Spalte Z.B: 12 ===>>   ").upper()
        if int(o[0]) == 1:
            if a[int(o[1])-1] == "E":
                a[int(o[1])-1] = "O"
                print(a, b, c, sep="\n")
            else:
                o = input(
                    "O bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12===>>   ").upper()
        elif int(o[0]) == 2:
            if b[int(o[1])-1] == "E":
                b[int(o[1])-1] = "O"
                print(a, b, c, sep="\n")
            else:
                o = input(
                    "O bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12===>>   ").upper()

        elif int(o[0]) == 3:
            if c[int(o[1])-1] == "E":
                c[int(o[1])-1] = "O"
                print(a, b, c, sep="\n")
            else:
                o = input(
                    "O bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12  ===>>   ").upper()
