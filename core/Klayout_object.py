import pya

class Klayout():
    def __init__(self,layer):
        self.layout = pya.Layout()
        self.top = self.layout.create_cell("TOP")
        self.layer = [self.layout.layer(i,0) for i in range(layer)] #layer层数设置

        self.Const = float(1e3)
        self.geometries = []

    def add(self,geometry):
        self.geometries.append(geometry)


    def draw(self):
        geometries = []
        for i in self.geometries:
            geometries += i.getDescendantList()
        for geometry in geometries:
            vtx = (geometry.position @ geometry.transform[:2, :2] + geometry.transform[:2, 2]) * self.Const
            points = [pya.Point.new(vtx[i][0], vtx[i][1]) for i in range(len(vtx))]
            self.top.shapes(self.layer[geometry.layer]).insert(pya.SimplePolygon.new(points))

    def write(self, name):
        self.layout.write(name)