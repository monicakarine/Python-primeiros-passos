class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    @property
    def position(self):
        return self.__x, self.__y

    def move(self, xoffset, yoffset):
        self.__x += xoffset
        self.__y += yoffset
    
    def __add__(self,another_point):
        return Point(self.__x + another_point.__x, self.__y + another_point.__y)

    def __str(self):
        return "({0},{1})".format(self.__x,self.__y)

p1 = Point(2,2)
p2 = Point(3,3)

p3 = p1 + p2

x, y = p1.position
print(x,y)

p1.move(1,1)

print(p1,p2,p3)

