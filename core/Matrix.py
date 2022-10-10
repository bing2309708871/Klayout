import numpy
from math import sin, cos

class Matrix(object):

    @staticmethod
    def makeIdentity(): # 单位矩阵
        return numpy.array([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]]).astype(float)

    @staticmethod
    def makeTranslation(x, y): # 移动矩阵
        return numpy.array([[1, 0, x],
                            [0, 1, y],
                            [0, 0, 1]]).astype(float)

    @staticmethod
    def makeRotation(angle): # 顺时针选择矩阵
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, s, 0],
                            [-s, c, 0],
                            [0, 0, 1]]).astype(float)

    @staticmethod
    def makeSymmetricX(): # x轴对称变换
        return numpy.array([[1, 0, 0],
                            [0, -1, 0],
                            [0, 0, 1]]).astype(float)

    @staticmethod
    def makeSymmetricY(): # y轴对称变换
        return numpy.array([[-1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]]).astype(float)


    @staticmethod
    def makeScale(s): # 缩放矩阵
        return numpy.array([[s, 0, 0],
                            [0, s, 0],
                            [0, 0, 1]]).astype(float)
