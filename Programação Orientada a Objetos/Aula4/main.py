from abc import ABC, abstractmethod
class Poligono(ABC):

    def __init__(self,cor,lados):
        self.__cor = cor
        self.__lados = lados
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def lados(self):
        return self.__lados

    @abstractmethod
    def area(self):
        pass

class Triangulo(Poligono):

    def __init__(self, cor, lados, base, altura):
        super().__init__(cor, lados)
        self.__base = base 
        self.__altura = altura
    
    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    def area(self):
        return(self.base*self.altura)/2

#poligono = Poligono()  não posso instanciar uma classe abstrata
triangulo = Triangulo('vermelho',3,12,8)
print(triangulo.cor, triangulo.lados,triangulo.base,triangulo.altura)
print(triangulo.area())