class Pessoa:
	def __init__(self,cor,residencia,sexo):
		self.cor = cor 
		self.residencia = residencia
		self.sexo = sexo
	def __str__(self):
		return 'A cor é {} e mora na {} e tem sexo {}.'.format(self.cor, self.residencia, self.sexo)
class Filha(Pessoa):
	def __init__(self,cor,residencia,sexo,cor_cabelo):
		super().__init__(self,cor,residencia,sexo)
		self.cor_cabelo = cor_cabelo
		
class Neta(Filha):
	def __init__(self,cor,residencia,sexo,cor_cabelo):
		super().__init__(self,cor,residencia,sexo,cor_cabelo)
p = Pessoa('Preta','Minha casa','Masculino')
print(p)

f = Filha('Preta','Minha casa', 'Feminino', 'Preto')
print(f.cor_cabelo);

n = Neta('merena','Minha casa', 'Feminino', 'loiro')
print(f.cor_cabelo,'\n',f.cor);
