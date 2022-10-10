from core import *
import numpy as np
import copy

# 建立一个Klayour类
layout = Klayout(100)

Rect = Rectangle()
rect = np.array([-1,1,-1,1])
Rect.add(Rectangle(rect=rect))
Rect.move([3,3])
Rect2 = copy.deepcopy(Rect)
Rect2.rotate(3.14/6)
Rect2.scale(4)

Rect3 = Rectangle()
Rect3.add(Rect2)

Poly = Polygon(vtx=[[1,0],[1,1],[0,0]])
# Poly.move([3,1])
Rect3.add(Poly)
Rect3.add(Ring(0,0,3,1,0,1))
Rect3.add(Sector(4,0,3,0,1))
Rect3.scale(1)
# Rect3.move([3,1])
Rect3.sysmetric()
layout.add(Rect3)
layout.draw()

layout.write("test1.gds")
