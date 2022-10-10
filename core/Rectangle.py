from core.Object2D import Object2D
import numpy as np

# 输入参数
# layer:在第几次绘图，默认第0层
# rect：矩形坐标信息


class Rectangle(Object2D):
    def __init__(self, layer = 0,rect=np.zeros(4)):
        super().__init__()
        self.name = 'Rectangle'
        self.layer = layer
        self.position = np.array([[rect[0], rect[2]],
                                   [rect[0], rect[3]],
                                   [rect[1], rect[3]],
                                   [rect[1], rect[2]]])
