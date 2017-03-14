class Rectangle:
    def __init__(self):
        self.x = 10.0
        self.y = 10.0
        self.x0 = 0.0
        self.y0 = 0.0

    def size(self):
        return (self.x,self.y)

    def resize(self,x,y):
        self.x = x
        self.y = y
    def recenter(self,x0,y0):
        self.x0 = x0
        self.y0 = y0

def overlap(A,B):
    distX = abs(A.x0 - B.x0)
    distY = abs(A.y0 - B.x0)
    if (A.x + B.x) > 2*distX:
        if (A.y + B.y) > 2*distY:
            return True
    return False
