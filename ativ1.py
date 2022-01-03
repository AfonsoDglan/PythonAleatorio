from abc import ABC, abstractmethod

class Funcionario(ABC):

    @abstractmethod
    def CalcularSalario(self):
        pass

class Gerente(Funcionario):
    def __init__(self,nome,matricula,salario_base):
        self.nome = nome;
        self.matricula = matricula;
        self.salario_base = salario_base

    def CalcularSalario(self):
        return self.salario_base * 2;

class Assistente(Funcionario):
    def __init__(self,nome,matricula,salario_base):
        self.nome = nome;
        self.matricula = matricula;
        self.salario_base = salario_base

    def CalcularSalario(self):
        return  self.salario_base

class Vendedor(Funcionario):
    def __init__(self,nome,matricula,salario_base,comicao):
        self.nome = nome;
        self.matricula = matricula;
        self.salario_base = salario_base
        self.comicao = comicao

    def CalcularSalario(self):
        return  self.salario_base + self.comicao;

if __name__ == '__main__':
    lista = [];
    gere = Gerente('Afonso', 1234, 1000);
    lista.append(gere);
    assis = Assistente('Paulo', 2345, 1000);
    lista.append(assis);
    vend = Vendedor('Gabriel', 4567, 1000, 50);
    lista.append(vend);

    print(f'Gerente: {lista[0].CalcularSalario()}');
    print(f'Assistente: {lista[1].CalcularSalario()}');
    print(f'Vendedor: {lista[2].CalcularSalario()}');


