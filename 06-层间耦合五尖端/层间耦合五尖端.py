from core import *
from core.Klayout_devices import *
import numpy as np
import copy

# 建立一个Klayour类
layout = Klayout(layer=2)

# 输入x轴对称梯形的上底，下底和高，返回四个顶点坐标
def get_vtx(W_ini, W_end, L):
    vtx = np.array([[0, -W_ini / 2],
                    [0, W_ini / 2],
                    [L, W_end / 2],
                    [L, -W_end / 2]])
    return vtx

R_Si_radius = 100
R_Si_think = 0.5

ring = Rectangle()
ring.add(Ring(x=0,
              y=-R_Si_radius,
              radius=R_Si_radius,
              think=R_Si_think,
              theta_start=0,
              theta_stop=np.pi/2))

ring.add(Ring(x=2*R_Si_radius,
              y=-R_Si_radius,
              radius=R_Si_radius,
              think=R_Si_think,
              theta_start=np.pi,
              theta_stop=3 * np.pi / 2))


head = draw_five_tips()
head.move([0,10])
head.sysmetric('X')
head.rotate(np.pi/4)
layout.add(head)
layout.add(ring)

head2 = copy.deepcopy(head)
head2.move([20,20])
layout.add(head2)

layout.draw()
layout.write("test.gds")