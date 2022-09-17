//pythonfile1
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[0][4] = "Not very effective"
advantagearray[0][5] = "Not very effective"
advantagearray[0][7] = "Super effective"
advantagearray[0][11] = "Super effective"
advantagearray[0][12] = "Super effective"
advantagearray[0][13] = "Not very effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "gub":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile2
advantagearray = [[0 for i in range(15)] for j in range(15)]

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "nogard":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile3
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[2][2] = "Not very effective"
advantagearray[2][5] = "Super effective"
advantagearray[2][7] = "Not very effective"
advantagearray[2][8] = "No effect"
advantagearray[2][14] = "Super effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "cirtcele":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile4
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[3][5] = "Not very effective"
advantagearray[3][6] = "No effect"
advantagearray[3][9] = "Super effective"
advantagearray[3][10] = "Super effective"
advantagearray[3][12] = "Not very effective"
advantagearray[3][13] = "Super effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "gnithgif":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile5
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[4][0] = "Super effective"
advantagearray[4][7] = "Super effective"
advantagearray[4][9] = "Super effective"
advantagearray[4][13] = "Not very effective"
advantagearray[4][14] = "Not very effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "erif":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile6
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[5][0] = "Super effective"
advantagearray[5][2] = "Not very effective"
advantagearray[5][3] = "Super effective"
advantagearray[5][7] = "Super effective"
advantagearray[5][13] = "Not very effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "gniylf":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile7
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[6][10] = "No effect"
advantagearray[6][12] = "No effect"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "tsohg":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile8
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[7][0] = "Not very effective"
advantagearray[7][4] = "Not very effective"
advantagearray[7][5] = "Not very effective"
advantagearray[7][7] = "Not very effective"
advantagearray[7][8] = "Super effective"
advantagearray[7][11] = "Not very effective"
advantagearray[7][13] = "Super effective"
advantagearray[7][14] = "Super effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "ssarg":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile9
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[8][2] = "Super effective"
advantagearray[8][4] = "Super effective"
advantagearray[8][5] = "No effect"
advantagearray[8][7] = "Not very effective"
advantagearray[8][11] = "Super effective"
advantagearray[8][13] = "Super effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "dnuorg":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile10
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[9][1] = "Super effective"
advantagearray[9][5] = "Super effective"
advantagearray[9][7] = "Super effective"
advantagearray[9][8] = "Super effective"
advantagearray[9][9] = "Not very effective"
advantagearray[9][14] = "Not very effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "eci":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile11
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[10][6] = "No effect"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "lamron":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")


//pythonfile12
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[11][0] = "Super effective"
advantagearray[11][7] = "Super effective"
advantagearray[11][8] = "Not very effective"
advantagearray[11][11] = "Not very effective"
advantagearray[11][13] = "Not very effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "nosiop":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile13
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[12][3] = "Super effective"
advantagearray[12][11] = "Super effective"
advantagearray[12][12] = "Not very effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "cihcysp":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile14
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[13][0] = "Super effective"
advantagearray[13][3] = "Not very effective"
advantagearray[13][4] = "Super effective"
advantagearray[13][5] = "Super effective"
advantagearray[13][9] = "Super effective"
advantagearray[13][13] = "Not very effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "kcor":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")

//pythonfile15
advantagearray = [[0 for i in range(15)] for j in range(15)]
advantagearray[14][4] = "Super effective"
advantagearray[14][7] = "Not very effective"
advantagearray[14][8] = "Super effective"
advantagearray[14][9] = "Not very effective"
advantagearray[14][13] = "Super effective"

import os

typearray = {
    "gub": 0,
    "nogard": 1,
    "cirtcele": 2,
    "gnithgif": 3,
    "erif": 4,
    "gniylf": 5,
    "tsohg": 6,
    "ssarg": 7,
    "dnuorg": 8,
    "eci": 9,
    "lamron": 10,
    "nosiop": 11,
    "cihcysp": 12,
    "kcor": 13,
    "retaw": 14
}

f = open("inputs.txt")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()

if line1 != "retaw":
    print("Type error")
else:
    ind1 = typearray.get(line1)
    ind2 = typearray.get(line2)
    if advantagearray[ind1][ind2] == 0:
        print("No type advantage")
    else:
        print(advantagearray[ind1][ind2])
f.close()
os.remove("inputs.txt")
