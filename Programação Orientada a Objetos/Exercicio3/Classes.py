class Item():
    def __init__(self,nome,valor):
        self.__nome = nome
        self.__valor = valor 
    @property
    def nome(self):
        return self.__nome
    @property
    def valor_sem_desconto(self):
        return self.__valor
    @property
    def valor_com_desconto(self):
        return self.valor_sem_desconto*(1 - self.desconto_item())
    
    def desconto_item(self):
        pass
        
    def tipo_item(self):
        pass

class Livro(Item):
        def __init__(self,nome, valor, desconto = 0.03):
            super().__init__(nome,valor)
            self.desconto = desconto 
        
        def desconto_item(self):
            return self.desconto
        
        def tipo_item(self):
            return "Livro"

class Brinquedo(Item):
        def __init__(self,nome,valor,desconto = 0.05):
            super().__init__(nome,valor)
            self.desconto = desconto 

        def desconto_item(self):
            return self.desconto

        def tipo_item(self):
            return "Brinquedo"

class Eletronico(Item):
        def __init__(self,nome,valor,desconto = 0.08):
            super().__init__(nome,valor)
            self.desconto = desconto 

        def desconto_item(self):
            return self.desconto

        def tipo_item(self):
            return "Eletronico"

class CestaCompras(Item):

    def __init__(self):
        self.itens = {}
        self.qtde = 0

    def adicionar_item(self,item,qtde):
        self.itens[item] = qtde 
        #self.qtde.append(qtde)

    def relatorio_final(self):
        #y=0
        valor_total_compra_desconto = 0
        for item,qtde in self.itens.items():
            valor_total_compra_desconto += (qtde*item.valor_com_desconto)
        print("%.2f" %valor_total_compra_desconto)

        for item,qtde in self.itens.items():
                print("%s, %s, %i, %.2f, %.2f %.2f" % (item.tipo_item(),item.nome, qtde, item.valor_sem_desconto, (qtde*item.valor_sem_desconto), (qtde*item.valor_com_desconto)))


livro1 = Livro("Senhor dos Aneis", 15.00)
brinq1 = Brinquedo("Carrinho", 12.99)
cesta = CestaCompras()
cesta.adicionar_item(livro1, 3)
cesta.adicionar_item(brinq1, 4)
 
cesta.relatorio_final()