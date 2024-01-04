import math
import numpy as np
from AcousticPara import Coord

def compute_angle(coordS,coordR):
    x = (coordR.lon - coordS.lon) * (111 * math.cos(coordS.lat / 180 * math.pi))
    y = (coordR.lat - coordS.lat) * 111
    R = math.sqrt(x * x + y * y)
    if y > 0:
        azi = math.atan(x / y)
    elif y == 0:
        azi = np.sign(x) * math.pi / 2
    else:
        azi = math.atan(x / y) + math.pi
    # if azi < 0:
    #     azi = azi + 2 * math.pi
    # return azi, R


s = Coord(132.2278, 22.69225)
p = [Coord(132.1153, 22.818918),
     Coord(132.1153, 22.782024),
     Coord(132.25012, 22.818918),
     Coord(132.25012, 22.782024)]



azi = []
for i in range(4):
    azi1, R1 = compute_angle(s, p[i])
    azi1 = azi1 * 180.0 / np.pi
    azi.append(azi1)

max1=max(azi)
min1 = min(azi)
print(azi)

test = []
for i in range(4):
    azi1, R1 = compute_angle(p[i], s)
    azi1 = azi1 * 180.0 / np.pi
    test.append(azi1)

print(test)

'''
[-39.331095353961594, -49.141952354017725, 9.233704829874934, 12.91893337497655]
[140.69494926913902, 130.87666309630018, 189.22529352893423, 192.9107375445085]


[320.6689046460384, 310.8580476459823, 9.233704829874934, 12.91893337497655]
[140.69494926913902, 130.87666309630018, 189.22529352893423, 192.9107375445085]
'''