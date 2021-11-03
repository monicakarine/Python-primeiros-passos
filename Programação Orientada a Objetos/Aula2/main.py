import math

class Autor:

        def __init__(self,nome,cpf):
            self.nome = nome 
            self.cpf = cpf

            self.colaboradores = []
        
        def adicionar_colaborador(self,colaborador):
            self.colaboradores.append(colaborador)

        def __repr__(self):
            return "Nome %s CPF: %s" %(self.nome,self.cpf)

class Livro:

    def __init__(self,titulo,ano,autor):
        self.titulo = titulo
        self.ano = ano 
        self.autor = autor

    def __str__(self):
        return "Titulo: " + self.titulo + "Autor: " + self.autor.nome

autor_joao = Autor("João da Silva",123456789)
livro = Livro("Livro do João",2020,autor_joao)
#print(livro)

autora_maria = Autor("Maria Souza",111112222)
autor_claudio= Autor("Claudio Matos", 99999999)

autor_joao.adicionar_colaborador(autora_maria)
autor_joao.adicionar_colaborador(autor_claudio)
print(autor_joao.colaboradores)