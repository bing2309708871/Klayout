import numpy as np
from graphics.Rectangle import Rectangle
from graphics.Polygon import Polygon


# 输入x轴对称梯形的上底，下底和高，返回四个顶点坐标
def get_vtx(W_ini, W_end, L):
    vtx = np.array([[0, -W_ini / 2],
                    [0, W_ini / 2],
                    [L, W_end / 2],
                    [L, -W_end / 2]])
    return vtx


# 五尖端器件参数初始化
L_extra = 100
G_ini = 0.952
W_ini = 0.351
G_end = 0.2
W_end = 1.103
L_tip = 13.235
W_comb1_ini = 2 * G_end + 3 * W_end
W_comb2_ini = G_end + 2 * W_end
W_comb1_end = 0.9
W_comb2_end = 0.2
L_SiN1_comb = 25
L_SiN2_comb = 20.68


def draw_five_tips():  # 五尖端部分

    # 五尖端
    tips5 = Rectangle()
    vtx = get_vtx(W_ini, W_end, L_tip)
    tips5.add(Polygon(vtx=vtx, move=[-L_tip, 0]))
    tips5.add(Polygon(vtx=vtx, move=[-L_tip, W_end + G_end]))
    tips5.add(Polygon(vtx=vtx, move=[-L_tip, -(W_end + G_end)]))
    tips5.add(Polygon(vtx=vtx, layer=1, move=[-L_tip, (W_end + G_end) / 2]))
    tips5.add(Polygon(vtx=vtx, layer=1, move=[-L_tip, -(W_end + G_end) / 2]))

    # 五尖端多出的矩形部分
    tip_rect = Rectangle()
    tip_rect.add(Rectangle(rect=np.array([-L_extra, 0, -W_ini / 2, W_ini / 2])))
    tip_rect.add(Rectangle(rect=np.array([-L_extra, 0, -W_ini / 2 + W_end + G_end, W_ini / 2 + W_end + G_end])))
    tip_rect.add(Rectangle(rect=np.array([-L_extra, 0, -W_ini / 2 - (W_end + G_end), W_ini / 2 - (W_end + G_end)])))
    tip_rect.add(
        Rectangle(rect=np.array([-L_extra, 0, -W_ini / 2 + (W_end + G_end) / 2, W_ini / 2 + (W_end + G_end) / 2]),
                  layer=1))
    tip_rect.add(
        Rectangle(rect=np.array([-L_extra, 0, -W_ini / 2 - (W_end + G_end) / 2, W_ini / 2 - (W_end + G_end) / 2]),
                  layer=1))
    tip_rect.move([-L_tip, 0])

    # 倒锥
    taper = Rectangle()
    vtx = get_vtx(W_comb1_ini, W_comb1_end, L_SiN1_comb)
    taper.add(Polygon(vtx=vtx))
    vtx = get_vtx(W_comb2_ini, W_comb2_end, L_SiN2_comb)
    taper.add(Polygon(vtx=vtx, layer=1))
    head = Rectangle()
    head.add(tips5)
    head.add(tip_rect)
    head.add(taper)
    return head


def draw_lines():  # 标记线
    lines = Rectangle()
    w = 5
    for i in range(21):
        if i in [0, 5, 15, 20]:
            h = 100
        elif i == 10:
            h = 150
        else:
            h = 50
        rect = np.array([2 * i * w, w + 2 * i * w, -h / 2, h / 2])
        lines.add(Rectangle(rect=rect))
    return lines
