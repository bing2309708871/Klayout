from Klayout_object import *
from Klayout_devices import *

# 建立一个Klayour类
layout = Klayout()


# 打印器件总长度
length = 3700
print("length=" + str(length) + "um")

# 参数初始化
L_extra = 100
R_ring = 100

# 参数初始化
number_of_ring = 1
L_add = 20
W_add = 100
L_waveguide = (length - (2 * L_SiN1_comb+2*L_tip+2*L_extra + (number_of_ring-0.5) * 4 * R_ring+(number_of_ring-0.5)*2*W_add)) / 2
Layer_think = 0.4
X_shitf = (number_of_ring-0.5)*(4*R_ring+2*W_add)+(L_extra+L_tip+L_SiN1_comb+L_waveguide)

# 输入x轴对称梯形的上底，下底和高，返回四个顶点坐标
def get_vtx(W_ini, W_end, L):
    vtx = np.array([[0, -W_ini / 2],
                    [0, W_ini / 2],
                    [L, W_end / 2],
                    [L, -W_end / 2]])
    return vtx


def draw_base(number):

    draw_five_tips(number,layout)

    # 第一层taper后接的波导
    rect = np.array([L_SiN1_comb, L_SiN1_comb + L_waveguide, -W_comb1_end / 2, W_comb1_end / 2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide', rect=rect))

    layout.move_name(str(number) + '_SiN', -(L_SiN1_comb + L_waveguide), 0)
    layout.rotation_name(str(number) + '_SiN',is_copy=True)
    layout.move_name('copy_'+str(number), (number_of_ring-0.5) * (4 * R_ring+2*W_add), 2*R_ring+L_add)

    for i in range(number_of_ring):
        layout.add_ring(ring(str(number) + "_SiN_ring1_" + str(i),
                             x=i * (4 * R_ring+2*W_add),
                             y=R_ring,
                             radius=R_ring,
                             think=W_comb1_end,
                             theta_start=np.pi / 2,
                             theta_stop=np.pi))

        rect = np.array(
            [2*i*W_add-W_comb1_end / 2 + (1 + i * 4) * R_ring, 2*i*W_add+W_comb1_end / 2 + (1 + i * 4) * R_ring, R_ring, L_add + R_ring])
        layout.add_rectange(rectange(str(number) + '_SiN_waveguide1_' + str(i), rect=rect))



        layout.add_ring(ring(str(number) + "_SiN_ring2_" + str(i),
                             x=(2 + 4 * i) * R_ring+2*i*W_add,
                             y=R_ring + L_add,
                             radius=R_ring,
                             think=W_comb1_end,
                             theta_start=-np.pi / 2,
                             theta_stop=0))

        rect = np.array(
            [2*i*W_add+(2 + i * 4) * R_ring, (1+2*i)*W_add + (2 + i * 4) * R_ring, L_add+2*R_ring-W_comb1_end/2, L_add+2*R_ring+W_comb1_end/2])
        layout.add_rectange(rectange(str(number) + '_SiN_waveguide2_' + str(i), rect=rect))

        if not i == number_of_ring-1:
            layout.add_ring(ring(str(number) + "_SiN_ring3_" + str(i),
                                 x=(1+2*i)*W_add+(2 + 4 * i) * R_ring,
                                 y=R_ring + L_add,
                                 radius=R_ring,
                                 think=W_comb1_end,
                                 theta_start=0,
                                 theta_stop=np.pi / 2))

            rect = np.array(
                [-W_comb1_end / 2 +(1+2*i)*W_add+ (3 + 4 * i) * R_ring, W_comb1_end / 2 +(1+2*i)*W_add+ (3 + 4 * i) * R_ring, R_ring, L_add + R_ring])
            layout.add_rectange(rectange(str(number) + '_SiN_waveguide3_' + str(i), rect=rect))

            layout.add_ring(ring(str(number) + "_SiN_ring4_" + str(i),
                                 x=(1+2*i)*W_add+4 * (i + 1) * R_ring,
                                 y=R_ring,
                                 radius=R_ring,
                                 think=W_comb1_end,
                                 theta_start=np.pi,
                                 theta_stop=3 * np.pi / 2))

            rect = np.array(
                [(1+2*i)*W_add+(i+1) * 4 * R_ring, 2*(i+1)*W_add + ( i+1) * 4 * R_ring, -W_comb1_end/2, W_comb1_end/2])
            layout.add_rectange(rectange(str(number) + '_SiN_waveguide4_' + str(i), rect=rect))

    draw_lines(layout,number)
    layout.move_name(str(number) + '_SiN_lines',x=-(L_extra+L_tip+L_SiN1_comb+L_waveguide)-50,y=L_add+R_ring)
    layout.move_name(str(number) + '_SiN_lines', x=X_shitf +(L_extra+L_tip+L_SiN1_comb+L_waveguide)-100-5, y=-L_add/2, is_copy=True)


draw_base(1)

draw_base(2)
layout.move_name('2_SiN', 0, 1500)
draw_base(3)
layout.move_name('3_SiN', 0, 3000)
draw_base(4)
layout.move_name('4_SiN', 0, 4500)
draw_base(5)
layout.move_name('5_SiN', 0, 6000)

w = 150
h=7000
rect = np.array([-w-(L_extra+L_tip+L_SiN1_comb+L_waveguide), -(L_extra+L_tip+L_SiN1_comb+L_waveguide), -1000, h])
layout.add_rectange(rectange('SiN_boundry1', rect=rect,z=1.5))

rect = np.array([X_shitf,X_shitf+w, -1000, h])
layout.add_rectange(rectange('SiN_boundry2', rect=rect,z=1.5))

layout.draw_polygon()
layout.draw_rectange()
layout.draw_ring(80)
layout.write("单环五尖端EC.gds")
