from core import *
import numpy as np

# 建立一个Klayour类
layout = Klayout(layer=2)


R_number = 10
R_radius = 30
R_thick = 0.7
R_gap = 2*R_thick
R_theta = 2*np.pi/9
W_taper_ini = 4.65
W_taper_end = 0.7
L_taper = 50
L_waveguide=10
R_ring = 100
L_add= 27

Y_shift = 100


# 输入x轴对称梯形的上底，下底和高，返回四个顶点坐标
def get_vtx(W_ini, W_end, L):
    vtx = np.array([[0, -W_ini / 2],
                    [0, W_ini / 2],
                    [L, W_end / 2],
                    [L, -W_end / 2]])
    return vtx

def draw_base():

    ring = Rectangle()
    for i in range(R_number):
        ring.add(Ring(x=-i*R_gap,
                      y=0,
                      radius=R_radius,
                      think=R_thick,
                      theta_start=-np.pi / 2 - R_theta / 2,
                      theta_stop=-np.pi / 2 + R_theta / 2,
                      # port_type=1,
                      elliptical=W_taper_ini))
    for i in range(R_number):
        ring.add(Ring(x=-(i-1)*R_gap,
                    y=0,
                    radius = R_radius,
                    think = R_thick,
                    theta_start=-np.pi/2-R_theta/2,
                    theta_stop=-np.pi/2+R_theta/2,
                    # port_type=1,
                    elliptical=W_taper_ini,
                    layer=1))
    ring.add(Sector(x=R_gap,
                     y=0,
                     radius=R_radius,
                     theta_start=-np.pi / 2 - R_theta / 2,
                     theta_stop=-np.pi / 2 + R_theta / 2,
                     elliptical=W_taper_ini))

    ring.move([-R_gap,0])

    return ring

ring = draw_base()
ring.scale(10)
ring.rotate(np.pi/2.3)
layout.add(ring)
layout.draw()
layout.write("test.gds")
