import math
import numpy as np

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
    return azi, R


s = (132.2278, 22.69225)
r = [(132.1153, 22.818918),
     (132.1153, 22.782024),
     (132.25012, 22.818918),
     (132.25012, 22.782024)]



azi = []
for i in range(4):
    azi1, R1 = compute_angle(s, r[i])
    azi1 = azi1 * 180.0 / np.pi
    azi.append(azi1)

print(azi)