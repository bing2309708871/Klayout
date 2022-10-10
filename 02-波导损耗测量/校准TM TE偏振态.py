from Klayout_object import *

# 建立一个Klayour类
layout = Klayout()

# 打印器件总长度
length = 3500
print("length=" + str(length) + "um")

# 参数初始化
W_comb1_ini = 0.18
W_comb1_end = 0.45
L_SiN1_comb = 200
R_ring = 10
number_of_ring = 66
L_add = 2
W_add = 2
L_waveguide = (length - (2 * L_SiN1_comb + number_of_ring * 4 * R_ring+number_of_ring*2*W_add)) / 2
Layer_think = 0.4


# 输入x轴对称梯形的上底，下底和高，返回四个顶点坐标
def get_vtx(W_ini, W_end, L):
    vtx = np.array([[0, -W_ini / 2],
                    [0, W_ini / 2],
                    [L, W_end / 2],
                    [L, -W_end / 2]])
    return vtx


def draw_base(number):
    # taper
    vtx = get_vtx(W_comb1_ini, W_comb1_end, L_SiN1_comb)
    layout.add_polygon(polygon(str(number) + '_SiN1_taper', vtx=vtx))

    # 第一层taper后接的波导
    rect = np.array([L_SiN1_comb, L_SiN1_comb + L_waveguide, -W_comb1_end / 2, W_comb1_end / 2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide', rect=rect))

    layout.move_name(str(number) + '_SiN', -(L_SiN1_comb + L_waveguide), 0)
    layout.rotation_name(str(number) + '_SiN',is_copy=True)
    layout.move_name('copy_'+str(number), number_of_ring * (4 * R_ring+2*W_add), 0)

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


draw_base(1)

number_of_ring = 0
L_waveguide_old = L_waveguide
L_waveguide = (length - (2 * L_SiN1_comb + number_of_ring * 4 * R_ring+number_of_ring*2*W_add)) / 2
draw_base(2)
Y_shift = 2*R_ring+L_add
layout.move_name('2_SiN',L_waveguide-L_waveguide_old, -Y_shift)


layout.draw_polygon()
layout.draw_rectange()
layout.draw_ring(50)
layout.write("校准TM TE偏振态.gds")
