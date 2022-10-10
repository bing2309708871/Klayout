from Klayout_object import *

# 建立一个Klayour类
layout = Klayout()

# 输入x轴对称梯形的上底，下底和高，返回四个顶点坐标
def get_vtx(W_ini, W_end, L):
    vtx = np.array([[0, -W_ini / 2],
                    [0, W_ini / 2],
                    [L, W_end / 2],
                    [L, -W_end / 2]])
    return vtx

length = 3700

#A
W_SiN_waveguide1 = 0.4
L_SiN_waveduide1 = 200
#B
W_SiN_taper1_ini = 0.4
W_SiN_taper1_end = 0.9
L_SiN_taper1 = 200
#C
W_SiN_waveguide2 = W_SiN_taper1_end
L_SiN_waveguide2 = 100
#D
W_SiN_taper2_ini = W_SiN_waveguide2
W_SiN_taper2_end = 0.36
L_SiN_taper2 = 80

W_Si_taper1_ini = 0.2
W_Si_taper1_end = 0.5
L_Si_taper1 = L_SiN_taper2

L_Si_waveguide3 = 100
L_SiN_waveguide3 = 200
#E
R_Si_radius = 100
R_Si_think = W_Si_taper1_end
#F
W_Si_taper2_ini = W_Si_taper1_end
W_Si_taper2_end = 0.2
L_Si_taper2 = 200
#G
W_Si_waveguide = W_Si_taper2_end
L_Si_waveguide = 200

number_of_uion = 0
layer2 = 0.7

L_SiN_waveguide2 = length - L_SiN_waveduide1-L_SiN_taper1-L_SiN_taper2-number_of_uion*(L_Si_waveguide3+2*L_SiN_taper2+L_SiN_waveguide3)-2*R_Si_radius-L_Si_taper2-L_Si_waveguide
X_shift_right = 2*R_Si_radius+L_Si_taper2+L_Si_waveguide
X_shift_left = length - X_shift_right

def draw_base(number):

    #A
    rect = np.array([-L_SiN_waveduide1, 0, -W_SiN_waveguide1 / 2, W_SiN_waveguide1 / 2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide1', rect=rect))
    #B
    vtx = get_vtx(W_SiN_taper1_ini, W_SiN_taper1_end, L_SiN_taper1)
    layout.add_polygon(polygon(str(number) + '_SiN_taper1', vtx=vtx))
    #每新增一个器件都将坐标往右移，确保下一器件的x坐标起始值为0
    layout.move_name(str(number) + "_SiN_", x=-L_SiN_taper1, y=0)
    #C
    rect = np.array([0, L_SiN_waveguide2, -W_SiN_waveguide2 / 2, W_SiN_waveguide2 / 2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide2', rect=rect))
    layout.move_name(str(number) + "_SiN_", x=-L_SiN_waveguide2, y=0)
    #D

    vtx = get_vtx(W_SiN_taper2_ini, W_SiN_taper2_end, L_SiN_taper2)
    layout.add_polygon(polygon(str(number) + '_SiN_taper2', vtx=vtx))
    vtx = get_vtx(W_Si_taper1_ini, W_Si_taper1_end, L_Si_taper1)
    layout.add_polygon(polygon(str(number) + '_Si_taper1', vtx=vtx,z = layer2))
    layout.move_name(str(number) + "_Si", x=-L_SiN_taper2, y=0)

    for i in range(number_of_uion):
        #Si波导,连接两Si tpaer
        rect = np.array([0, L_Si_waveguide3, -W_Si_taper1_end / 2, W_Si_taper1_end / 2])
        layout.add_rectange(rectange(str(number) + '_Si_waveguide3', rect=rect,z=layer2))
        layout.move_name(str(number) + "_Si", x=-L_Si_waveguide3, y=0)

        #SiN与Si级联部分，与之前级联形状对称
        vtx = get_vtx(W_Si_taper1_end,W_Si_taper1_ini, L_Si_taper1)
        layout.add_polygon(polygon(str(number) + '_Si_taper1_1_'+str(i), vtx=vtx, z=layer2))
        vtx = get_vtx(W_SiN_taper2_end,W_SiN_taper2_ini, L_SiN_taper2)
        layout.add_polygon(polygon(str(number) + '_SiN_taper2_1_'+str(i), vtx=vtx))
        layout.move_name(str(number) + "_Si", x=-L_SiN_taper2, y=0)

        #SiN波导，连接两SiN taper
        rect = np.array([0, L_SiN_waveguide3, -W_SiN_taper2_ini / 2, W_SiN_taper2_ini / 2])
        layout.add_rectange(rectange(str(number) + '_SiN_waveguide3', rect=rect))
        layout.move_name(str(number) + "_Si", x=-L_SiN_waveguide3, y=0)

        # SiN与Si级联部分
        vtx = get_vtx(W_SiN_taper2_ini, W_SiN_taper2_end, L_SiN_taper2)
        layout.add_polygon(polygon(str(number) + '_SiN_taper2_1_'+str(i), vtx=vtx))
        vtx = get_vtx(W_Si_taper1_ini, W_Si_taper1_end, L_Si_taper1)
        layout.add_polygon(polygon(str(number) + '_Si_taper1_1_'+str(i), vtx=vtx, z=layer2))
        layout.move_name(str(number) + "_Si", x=-L_SiN_taper2, y=0)

    #E，S型走线，由两圆环组成
    layout.add_ring(ring(str(number) + "_Si_ring1",
                         x=0,
                         y=-R_Si_radius,
                         radius=R_Si_radius,
                         think=R_Si_think,
                         theta_start=0,
                         theta_stop=np.pi / 2,
                         z = layer2))
    layout.add_ring(ring(str(number) + "_Si_ring2",
                         x=2*R_Si_radius,
                         y=-R_Si_radius,
                         radius=R_Si_radius,
                         think=R_Si_think,
                         theta_start=np.pi,
                         theta_stop=3*np.pi / 2,
                         z = layer2))

    #F
    vtx = get_vtx(W_Si_taper2_ini, W_Si_taper2_end, L_Si_taper2)
    layout.add_polygon(polygon(str(number) + '_Si_taper2', vtx=vtx,move_x=2*R_Si_radius,move_y=-2*R_Si_radius,z = layer2))
    #G
    rect = np.array([0, L_Si_waveguide, -W_Si_waveguide / 2, W_Si_waveguide / 2])
    layout.add_rectange(rectange(str(number) + '_Si_waveguide1', rect=rect,z = layer2))
    layout.move_name(str(number) + "_Si_waveguide1", x=2*R_Si_radius+L_Si_taper2, y=-2*R_Si_radius)

    draw_lines(layout, number)
    layout.move_name(str(number) + '_SiN_lines', x=-X_shift_left - 50,y=100)
    layout.move_name(str(number) + '_SiN_lines', x=length-105,y=0, is_copy=True)

draw_base(1)

number_of_uion = 1
L_SiN_waveguide2 = length - L_SiN_waveduide1-L_SiN_taper1-L_SiN_taper2-number_of_uion*(L_Si_waveguide3+2*L_SiN_taper2+L_SiN_waveguide3)-2*R_Si_radius-L_Si_taper2-L_Si_waveguide
draw_base(2)
layout.move_name('2_Si', 0, 2000)

number_of_uion = 2
L_SiN_waveguide2 = length - L_SiN_waveduide1-L_SiN_taper1-L_SiN_taper2-number_of_uion*(L_Si_waveguide3+2*L_SiN_taper2+L_SiN_waveguide3)-2*R_Si_radius-L_Si_taper2-L_Si_waveguide
draw_base(3)
layout.move_name('3_Si', 0, 4000)

number_of_uion = 3
L_SiN_waveguide2 = length - L_SiN_waveduide1-L_SiN_taper1-L_SiN_taper2-number_of_uion*(L_Si_waveguide3+2*L_SiN_taper2+L_SiN_waveguide3)-2*R_Si_radius-L_Si_taper2-L_Si_waveguide
draw_base(4)
layout.move_name('4_Si', 0, 6000)

number_of_uion = 4
L_SiN_waveguide2 = length - L_SiN_waveduide1-L_SiN_taper1-L_SiN_taper2-number_of_uion*(L_Si_waveguide3+2*L_SiN_taper2+L_SiN_waveguide3)-2*R_Si_radius-L_Si_taper2-L_Si_waveguide
draw_base(5)
layout.move_name('5_Si', 0, 8000)


w = 150
h=9000

rect = np.array([-w-X_shift_left, -X_shift_left, -1000, h])
layout.add_rectange(rectange('SiN_boundry1', rect=rect,z=1.5))

rect = np.array([X_shift_right, X_shift_right+w, -1000, h])
layout.add_rectange(rectange('SiN_boundry2', rect=rect,z=1.5))

layout.draw_polygon()
layout.draw_rectange()
layout.draw_ring(80)
layout.write("多级联.gds")
