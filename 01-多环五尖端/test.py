from Klayout_devices import *

# 建立一个Klayour类
layout = Klayout()

# 打印器件总长度
length = 3700
print("length=" + str(length) + "um")

R_ring = 100
L_waveguide = (length - 2 * (L_tip + L_extra+L_SiN1_comb + 9 * R_ring)) / 2
Layer_think = 0.4
L_add = 0

# 绘制一个五尖端器件
def draw_base(number):

    draw_five_tips(number,layout)
    # 第一层taper波导
    rect = np.array([L_SiN1_comb, L_SiN1_comb + L_waveguide, -W_comb1_end / 2, W_comb1_end / 2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide', rect=rect))

    layout.add_ring(ring(str(number) + "_SiN_ring",
                         x=L_SiN1_comb + L_waveguide,
                         y=-R_ring,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=0,
                         theta_stop=np.pi / 2))

    layout.move_name(str(number) + '_SiN', -(L_SiN1_comb + L_waveguide + R_ring), R_ring)

    rect = np.array([-W_comb1_end / 2, W_comb1_end / 2, -L_add, 0])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide2', rect=rect))
    rect = np.array([-W_comb1_end / 2 + 2 * R_ring, W_comb1_end / 2 + 2 * R_ring, -L_add, 0])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide3', rect=rect))
    rect = np.array([-W_comb1_end / 2 + 4 * R_ring, W_comb1_end / 2 + 4 * R_ring, -L_add, 0])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide4', rect=rect))
    # rect = np.array([-W_comb1_end / 2 + 6 * R_ring, W_comb1_end / 2 + 6 * R_ring, -L_add, 0])
    # layout.add_rectange(rectange(str(number) + '_SiN_waveguide5', rect=rect))
    rect = np.array([-W_comb1_end / 2 + 8 * R_ring, W_comb1_end / 2 + 8 * R_ring, -L_add / 2, 0])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide6', rect=rect))

    layout.add_ring(ring(str(number) + "_SiN_ring2",
                         x=R_ring,
                         y=-L_add,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=np.pi / 2,
                         theta_stop=3 * np.pi / 2))

    layout.add_ring(ring(str(number) + "_SiN_ring3",
                         x=3 * R_ring,
                         y=0,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=-np.pi / 2,
                         theta_stop=np.pi / 2))
    layout.add_ring(ring(str(number) + "_SiN_ring4",
                         x=5 * R_ring,
                         y=-L_add,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=np.pi / 2,
                         theta_stop=3 * np.pi / 2))
    layout.add_ring(ring(str(number) + "_SiN_ring5",
                         x=7 * R_ring,
                         y=0,
                         radius=R_ring,
                         think=W_comb1_end,
                         theta_start=-np.pi / 2,
                         theta_stop=np.pi / 2))

    layout.move_name(str(number) + '_SiN', -8 * R_ring, L_add / 2)

    rect = np.array([-200.45, -199.55, -L_add/2, L_add/2])
    layout.add_rectange(rectange(str(number) + '_SiN_waveguide5', rect=rect))

    layout.rotation_name(str(number) + '_SiN', is_copy=True)

    draw_lines(layout,number)

    layout.move_name(str(number) + '_SiN_lines',x=-length/2-50,y=L_add/2)
    layout.move_name(str(number) + '_SiN_lines', x=length -100-5, y=-L_add, is_copy=True)


draw_base(1)
L_add = 500 / 2
draw_base(2)
layout.move_name('2_SiN', 0, 1500)

L_add = 1000 / 2
draw_base(3)
layout.move_name('3_SiN', 0, 3000)
L_add = 1500 / 2
draw_base(4)
layout.move_name('4_SiN', 0, 5000)
L_add = 2000 / 2
draw_base(5)
layout.move_name('5_SiN', 0, 7000)


w = 150
h=8500
rect = np.array([-w-length/2, -length/2, -1000, h])
layout.add_rectange(rectange('SiN_boundry1', rect=rect,z=1.5))

rect = np.array([w+length/2, length/2, -1000, h])
layout.add_rectange(rectange('SiN_boundry2', rect=rect,z=1.5))

layout.draw_polygon()
layout.draw_rectange()
layout.draw_ring(80)
layout.write("多环五尖端EC.gds")
