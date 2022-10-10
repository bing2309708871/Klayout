from Klayout_object import *

# 建立一个Klayour类
layout = Klayout()

# 打印器件总长度
length = 3700
print("length=" + str(length) + "um")

# 参数初始化
L_waveguide2 = 100
W_comb1_ini = 0.40
W_comb1_end = 0.9
L_SiN1_comb = 200
R_ring = 100
number_of_ring = 7
L_add = 0
W_add = 0
L_waveguide = (length - (2 * L_SiN1_comb +2*L_waveguide2 + (number_of_ring-0.5) * (4 * R_ring+2*W_add))) / 2
Layer_think = 0.4
layer2 = 0.7
layer3 = 1.2
layer4 = 1.7

X_shift_left = L_SiN1_comb+L_waveguide+L_waveguide2
X_shift_right = length-X_shift_left


# 输入x轴对称梯形的上底，下底和高，返回四个顶点坐标
def get_vtx(W_ini, W_end, L):
    vtx = np.array([[0, -W_ini / 2],
                    [0, W_ini / 2],
                    [L, W_end / 2],
                    [L, -W_end / 2]])
    return vtx


def draw_base(number):
    # 100um冗余保护直波导
    rect = np.array([-L_waveguide2, 0, -W_comb1_ini / 2, W_comb1_ini / 2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide2', rect=rect))
    # taper
    vtx = get_vtx(W_comb1_ini, W_comb1_end, L_SiN1_comb)
    layout.add_polygon(polygon(str(number) + '_SiN1_taper', vtx=vtx))

    # 第一层taper后接的波导
    rect = np.array([L_SiN1_comb, L_SiN1_comb + L_waveguide, -W_comb1_end / 2, W_comb1_end / 2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide', rect=rect))

    layout.move_name(str(number) + '_SiN', -(L_SiN1_comb + L_waveguide), 0)
    layout.rotation_name(str(number) + '_SiN',is_copy=True)
    if number_of_ring == 0:
        layout.move_name('copy_' + str(number), (number_of_ring - 0.5) * (4 * R_ring + 2 * W_add), 0)
    else:
        layout.move_name('copy_' + str(number), (number_of_ring - 0.5) * (4 * R_ring + 2 * W_add), 2 * R_ring + L_add)

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

    if not number_of_ring == 0:
        draw_lines(layout, number)
        layout.move_name(str(number) + '_SiN_lines', x=-X_shift_left - 50, y=100)
        layout.move_name(str(number) + '_SiN_lines', x=length - 105, y=0, is_copy=True)


draw_base(1)

number_of_ring = 0
L_waveguide_old = L_waveguide
L_waveguide = (length - (2 * L_SiN1_comb + number_of_ring * 4 * R_ring+number_of_ring*2*W_add)) / 2
draw_base(2)
Y_shift = 2*R_ring+L_add
layout.move_name('2_SiN',L_waveguide-L_waveguide_old, Y_shift+100)

number_of_ring = 7
L_add = 100
L_waveguide = (length - (2 * L_SiN1_comb + number_of_ring * 4 * R_ring+number_of_ring*2*W_add)) / 2
draw_base(3)
Y_shift = -2*R_ring-L_add - 100
layout.move_name('3_SiN',L_waveguide-L_waveguide_old, Y_shift)

L_add = 200
draw_base(4)
Y_shift = Y_shift -2*R_ring-L_add - 100
layout.move_name('4_SiN',L_waveguide-L_waveguide_old, Y_shift)

L_add = 400
draw_base(5)
Y_shift = Y_shift -2*R_ring-L_add- 100
layout.move_name('5_SiN',L_waveguide-L_waveguide_old, Y_shift)

L_add = 800
draw_base(6)
Y_shift = Y_shift -2*R_ring-L_add- 100
layout.move_name('6_SiN',L_waveguide-L_waveguide_old, Y_shift)

L_add = 1600
draw_base(7)
Y_shift = Y_shift -2*R_ring-L_add- 100
layout.move_name('7_SiN',L_waveguide-L_waveguide_old, Y_shift)

L_add = 2
# draw_base(8)
# Y_shift = Y_shift -2*R_ring-L_add- 100
# layout.move_name('8_SiN',L_waveguide-L_waveguide_old,  Y_shift)

number_of_ring = 0
L_waveguide_old = L_waveguide
L_waveguide = (length - (2 * L_SiN1_comb + number_of_ring * 4 * R_ring+number_of_ring*2*W_add)) / 2
draw_base(9)
Y_shift = Y_shift - 100
layout.move_name('9_SiN',L_waveguide-L_waveguide_old, Y_shift)


w = 150
h=5000

rect = np.array([-w-X_shift_left, -X_shift_left, -h, 500])
layout.add_rectange(rectange('SiN_boundry1', rect=rect,z=layer4))
rect = np.array([X_shift_right, X_shift_right+w, -h, 500])
layout.add_rectange(rectange('SiN_boundry2', rect=rect,z=layer4))

layout.draw_polygon()
layout.draw_rectange()
layout.draw_ring(50)
layout.write("波导损耗测量SiN.gds")
