from core.Matrix import Matrix
import numpy

class Object2D(object):
    def __init__(self):
        self.transform = Matrix.makeIdentity()
        self.parent = None
        self.children = []

    def add(self, child): #添加子图形
        self.children.append(child)
        child.parent = self

    def remove(self, child): # 去除图形
        self.children.remove(child)
        child.parent = None

    # 执行整个图形块的移动、旋转、放大、对称操作
    def move(self, Direction):
        for object in self.getDescendantList():
            object.set_translate(Direction[0],Direction[1],localCoord=False)

    def rotate(self,angle):
        for object in self.getDescendantList():
            object.set_rotate(angle,localCoord=False)

    def scale(self,s):
        for object in self.getDescendantList():
            object.set_scale(s,localCoord=False)

    def sysmetric(self,sysmetric='X'):
        for object in self.getDescendantList():
            if sysmetric == 'X':
                object.set_symmetricX(localCoord=False)
            else:
                object.set_symmetricY(localCoord=False)

    # 对单个图形执行移动、旋转、缩放、对称操作
    def set_translate(self, x, y, localCoord=True):
        m = Matrix.makeTranslation(x, y)
        self.applyMatrix(m, localCoord)

    def set_rotate(self, angle, localCoord=True):
        m = Matrix.makeRotation(angle)
        self.applyMatrix(m, localCoord)

    def set_scale(self, s, localCoord=True):
        m = Matrix.makeScale(s)
        self.applyMatrix(m, localCoord)

    def set_symmetricX(self, localCoord=True):
        m = Matrix.makeSymmetricX()
        self.applyMatrix(m, localCoord)

    def set_symmetricY(self, localCoord=True):
        m = Matrix.makeSymmetricY()
        self.applyMatrix(m, localCoord)


    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def getDescendantList(self):  # 得到所有子图形列表
        descendants = []
        nodesToProcess = [self]
        while len(nodesToProcess) > 0:
            node = nodesToProcess.pop(0)
            descendants.append(node)
            nodesToProcess = node.children + nodesToProcess
        return descendants

    # returns 2x2 submatrix with rotation data
    def getRotationMatrix(self):
        return numpy.array([self.transform[0][0:2],
                            self.transform[1][0:2]])

    # get/set position components of transform
    def getPosition(self):
        return [self.transform.item((0, 2)),
                self.transform.item((1, 2))]

    def getWorldPosition(self):
        worldTransform = self.getWorldMatrix()
        return [worldTransform.item((0, 2)),
                worldTransform.item((1, 2))]

    def getWorldMatrix(self):
        if self.parent == None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @self.transform

    def setPosition(self, position):
        self.transform.itemset((0, 3), position[0])
        self.transform.itemset((1, 3), position[1])