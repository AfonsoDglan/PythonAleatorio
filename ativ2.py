from abc import ABC,abstractmethod

class Cartao(ABC):

    @abstractmethod
    def showMessage(self):
        pass

class DiaDosNamorados(Cartao):
    def __init__(self,destinatario):
        self.destinatario = destinatario

    def showMessage(self):
        print(f'Feliz dia dos namorados {self.destinatario}.');

class Natal(Cartao):
    def __init__(self,destinatario):
        self.destinatario = destinatario

    def showMessage(self):
        print(f'Feliz natal {self.destinatario}.');

class Aniversario(Cartao):
    def __init__(self,destinatario):
        self.destinatario = destinatario

    def showMessage(self):
        print(f'Feliz aniversario {self.destinatario}.')

if __name__ == '__main__':
    lista = [];
    n1 = DiaDosNamorados('Julia');
    n2 = DiaDosNamorados('paulo');
    n3 = DiaDosNamorados('amanda');
    lista.append(n1);
    lista.append(n2);
    lista.append(n3);
    na1 = Natal('Mãe');
    na2 = Natal('Vó');
    na3 = Natal('Gabriela');
    lista.append(na1);
    lista.append(na2);
    lista.append(na3);
    ani1 = Aniversario('Luiza');
    ani2 = Aniversario('Daniel');
    ani3 = Aniversario('Marcos');
    lista.append(ani1);
    lista.append(ani2);
    lista.append(ani3);
    for x in lista:
        x.showMessage();

