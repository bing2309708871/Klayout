from core import *
from graphics import *

import copy
import numpy as np


# 打印器件总长度
length = 3700
print("length=" + str(length) + "um")

R_ring = 100
L_waveguide = (length - 2 * (L_tip + L_extra+L_SiN1_comb + 9 * R_ring)) / 2
Layer_think = 0.4
L_add = 0

# 绘制一个五尖端器件
def draw_base():
    base = Rectangle()

    five_tips = draw_five_tips()
    base.add(five_tips)

    # 第一层taper波导
    taper = Rectangle()
    rect = np.array([L_SiN1_comb, L_SiN1_comb + L_waveguide, -W_comb1_end / 2, W_comb1_end / 2])
    taper.add(Rectangle(rect=rect))
    taper.add(Ring(x=L_SiN1_comb + L_waveguide,
                         y=-R_ring,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=0,
                         theta_stop=np.pi / 2))
    base.add(taper)
    base.move([-(L_SiN1_comb + L_waveguide + R_ring), R_ring])

    S_line = Rectangle()
    rect = np.array([-W_comb1_end / 2, W_comb1_end / 2, -L_add, 0])
    S_line.add(Rectangle(rect=rect))
    rect = np.array([-W_comb1_end / 2 + 2 * R_ring, W_comb1_end / 2 + 2 * R_ring, -L_add, 0])
    S_line.add(Rectangle(rect=rect))
    rect = np.array([-W_comb1_end / 2 + 4 * R_ring, W_comb1_end / 2 + 4 * R_ring, -L_add, 0])
    S_line.add(Rectangle(rect=rect))
    rect = np.array([-W_comb1_end / 2 + 8 * R_ring, W_comb1_end / 2 + 8 * R_ring, -L_add / 2, 0])
    S_line.add(Rectangle(rect=rect))
    S_line.add(Ring(x=R_ring,
                         y=-L_add,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=np.pi / 2,
                         theta_stop=3 * np.pi / 2))
    S_line.add(Ring(x=3 * R_ring,
                         y=0,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=-np.pi / 2,
                         theta_stop=np.pi / 2))
    S_line.add(Ring(x=5 * R_ring,
                         y=-L_add,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=np.pi / 2,
                         theta_stop=3 * np.pi / 2))
    S_line.add(Ring(x=7 * R_ring,
                         y=0,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=-np.pi / 2,
                         theta_stop=np.pi / 2))

    base.add(S_line)
    base.move([-8 * R_ring, L_add / 2])


    rect = np.array([-200.45, -199.55, -L_add/2, L_add/2])
    base.add(Rectangle(rect=rect))
    base_copy = copy.deepcopy(base)
    base_copy.rotate(np.pi)
    base.add(base_copy)

    lines = draw_lines()
    lines.move([-length/2-50,L_add/2])
    lines2 = copy.deepcopy(lines)
    lines2.move([length -100-5, -L_add])
    lines.add(lines2)
    base.add(lines)

    return base

base1 = draw_base()

L_add = 500 / 2
base2 = draw_base()
base2.move([0,1500])

L_add = 1000 / 2
base3 = draw_base()
base3.move([0,3000])

L_add = 1500 / 2
base4 = draw_base()
base4.move([0,5000])

L_add = 2000 / 2
base5 = draw_base()
base5.move([0,7000])

w = 150
h=8500
rect = np.array([-w-length/2, -length/2, -1000, h])
base1.add(Rectangle(rect=rect,layer=1))
rect = np.array([w+length/2, length/2, -1000, h])
base1.add(Rectangle(rect=rect,layer=1))


# 建立一个Klayour类
layout = Layout(layer=2)
layout.add(base1)
layout.add(base2)
layout.add(base3)
layout.add(base4)
layout.add(base5)
layout.draw()

layout.write("多环五尖端EC.gds")
