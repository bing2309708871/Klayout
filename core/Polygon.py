from core.Object2D import Object2D
import numpy as np

class Polygon(Object2D):
    def __init__(self, layer=0,vtx=np.zeros(4),move=[0,0]):
        super().__init__()
        self.name = 'Polygon'
        self.layer = layer
        self.position = np.array(vtx)
        self.move(move)
