# Sequence　file を入力すると、NightTour が成り立っているか否か検証する。

import csv
import math

# SequencenXm.csv
filename = 'Sequence220.csv'

with open(filename, encoding='utf8', newline='') as f:

    csvl = csv.reader(f)

    content = [row for row in csvl] 

xsize = int(content[0][0])
ysize = int(content[1][0])
size = int(content[2][0])

table = [-1] * size

pos1 = int(content[3][0])

table[pos1] = pos1

for pos in content[4:] :
    
    pos2 = int(pos[0])

    x1 = pos1 % xsize
    y1 = pos1 // xsize

    x2 = pos2 % xsize
    y2 = pos2 // xsize

    abx = abs(x1-x2)
    aby = abs(y1-y2)

    if (abx == 1 and aby == 2) | (abx == 2 or aby == 1) :

        if table[pos2] == -1 :

            table[pos2] = pos2
    
            pos1 = pos2
            continue

    print("error")
    
print("ok")
