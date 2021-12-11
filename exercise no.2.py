class Circle:
    def __init__(self, radius=1.0, color="red") -> None:
        self.radius = radius
        self.color = color

    def getRadius(self) -> float:
        return self.radius

    def setRadius(self) -> float:
        self.radius = radius

    def getColor(self) -> str:
        return self.color

    def setColor(self) -> None:
        self.color = color

    def toString(self) -> str:
        pass

    def getArea(self) -> float:
        return self.radius**2 * 3.14

class Cylinder(Circle):
    def __init__(self, height=1.0, radius, color):
        super().__init__(radius, color)
        self.height = height

    def getHeight(self) -> float:
        return self.height

    def setHeight(self) -> None:
        self.height = height

    def toString(self) -> str:
        pass

    def getVolume(self) -> float:
        return self.radius*self.radius * 3.14 * self.height

# Note: I have no idea on the toString part and not sure for the setHeight