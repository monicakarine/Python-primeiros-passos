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
            x1 = max(min(self.esq_sup.x, self.dir_inf.x), min(ret.esq_sup.x, ret.dir_inf.x))
            y1 = max(min(self.esq_sup.y, self.dir_inf.y), min(ret.esq_sup.y, ret.dir_inf.y))
            x2 = min(max(self.esq_sup.x, self.dir_inf.x), max(ret.esq_sup.x, ret.dir_inf.x))
            y2 = min(max(self.esq_sup.y, self.dir_inf.y), max(ret.esq_sup.y, ret.dir_inf.y))
            if x1<x2 and y1<y2:
                r3_esq_sup = Ponto2D(x1, y1)
                r3_dir_inf = Ponto2D(x2, y2)
                ret3 = Retangulo(r3_esq_sup,r3_dir_inf)
                area3 = ret3.calcularArea()
                return area3
            else :
                return None

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


r1_esq_sup = Ponto2D(-7.0, 1.0)
r1_dir_inf = Ponto2D(7.0, -3.0)
ret1 = Retangulo(r1_esq_sup,r1_dir_inf)
area1 = ret1.calcularArea()
print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))

r2_esq_sup = Ponto2D(3.0, 3.0)
r2_dir_inf = Ponto2D(6.0, -2.0)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
area2 = ret2.calcularArea()
print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))

intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)



