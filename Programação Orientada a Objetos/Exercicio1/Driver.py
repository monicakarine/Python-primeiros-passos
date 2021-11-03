import math
from typing import TYPE_CHECKING

class Ponto2D:
        def __init__(self,x=0.0, y=0.0):
            self.x = x
            self.y = y

class Retangulo:
        def __init__(self,esq_sup, dir_inf):
            self.__esq_sup = esq_sup
            self.__dir_inf = dir_inf
        
        def calcularArea(self):
            area = self.width*self.height
            return area 

        def calcularIntersecao(self,ret):
            SI = max(0,min(ret.dir_inf.x, self.dir_inf.x) - max(ret.esq_sup.x, self.esq_sup.x)) * max(0,min(ret.dir_inf.y, self.dir_inf.y) - max(ret.esq_sup.y, self.esq_sup.y))
            if SI == 0:
                return None
            else:
                return SI

        @property 
        def esq_sup(self):
            return self.__esq_sup

        @property
        def dir_inf(self):
            return self.__dir_inf

        @property
        def width(self):
            width = abs(self.esq_sup.x - self.dir_inf.x)
            return width

        @property
        def height(self):
            height = abs(self.esq_sup.y - self.dir_inf.y)
            return height



r1_esq_sup = Ponto2D(-6.5, 5.0)
r1_dir_inf = Ponto2D(-2.0, 2.5)
ret1 = Retangulo(r1_esq_sup,r1_dir_inf)
area1 = ret1.calcularArea()
print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))

r2_esq_sup = Ponto2D(2.0, 7.0)
r2_dir_inf = Ponto2D(5.0, 4.0)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
area2 = ret2.calcularArea()
print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))

intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)



