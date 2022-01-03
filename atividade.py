from datetime import *

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome;
        self.idade = idade;
        self.altura = altura;
        self.peso = peso;

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,v):
        if isinstance(v, float):
            v = int(v);
        elif isinstance(v, str):
            i = int(input('Digite a idade novamente não pode ser uma string: '));
            v = i;
        if v < 0:
            while True:
                i = int(input('Digite a idade novamente não pode ser negativo: '));
                if i >= 0:
                    v = i;
                    break
                else:
                    continue
        self._idade = v
    @property
    def altura(self):
        return self._altura;

    @altura.setter
    def altura(self,x):
        if isinstance(x, int):
            x = float(x);
        elif isinstance(x, str):
            alt = float(input('Digite a altura novamente em metros: '));
            x = alt;
        if x < 0:
            while True:
                alt2 = float(input('Digite a altura novamente não pode ser negativo: '));
                if alt2 >= 0:
                    x = alt2;
                    break
                else:
                    continue
        self._altura = x
    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self,y):
        if isinstance(y,int):
            y = float(y);
        elif isinstance(y,str):
            pes = float(input('Digite o peso novamente em kilos: '));
            y = pes;
        if y < 0:
            while True:
                peso = float(input('Digite o peso novamente não pode ser negativo: '));
                if peso >= 0:
                    y = peso;
                    break
                else:
                    continue
        self._peso = y;

class Amigo(Pessoa):
    def __init__(self, nome, idade, altura, peso, nasc=date.today()):
        super(Amigo, self).__init__(nome,idade,altura,peso);
        self.nascimento = nasc;

    @property
    def nascimento(self):
        return self._nascimento;

    @nascimento.setter
    def nascimento(self,nac):
        nac = nac.split('/');
        atual = date.today();
        atual = atual.split('-');
        if date(int(nac[2]), int(nac[1]), int(nac[0])) < date(int(atual[2]), int(atual[1]), int(atual[0])):
            nac = '/'.split(nac);
        else:
            while True:
                data = str(input('Digite a data de nascimento certa 00/00/0000: '));
                data = data.split('/');
                atual = date.today();
                atual = atual.split('-');
                if date(int(data[2]), int(data[1]), int(data[0])) > date(int(atual[2]), int(atual[1]), int(atual[0])):
                    nac = '/'.split(nac);
                    break
                else:continue;

        self._nascimento = nac;

