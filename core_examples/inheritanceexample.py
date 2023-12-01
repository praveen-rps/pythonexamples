class Box2D:
	def __init__(self):
		self.length=1;
		self.breadth=2;
	def calArea(self):
	    print("The surface area is ", (self.length*self.breadth));


class Box3D(Box2D):
    def __init__(self):
        Box2D.__init__();
        self.height=3;
    def calVolume(self):
        print("The volume is :", super.length * super.breadth * self.height)

if __name__ == '__main__':
    box = Box3D();
    box.calArea();
    box.calVolume();