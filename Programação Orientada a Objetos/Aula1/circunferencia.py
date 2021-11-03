#Criando um método inicializador da circunferencia

import math

class Circ: 
        def __init__(self,x=0.0, y=0.0, r=1.0):
            self.x = x
            self.y = y
            self.r = r

        def area(self):
            return math.pi*self.r*self.r

        def __str__(self):
            return "Circunferencia: " + str(self.x) + "," + str(self.y) + "," + str(self.r)  

c1 = Circ(10,10,10); #objeto
a = c1.area()
print(a)
print(c1.x,c1.y,c1.r)
print(c1)
# dois underscore = private /// um underscore = protected
