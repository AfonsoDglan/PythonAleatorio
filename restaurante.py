#exemplo de como usar dicionario
#class Nome:
#  def __init__(self,nome,**outros):
#    self.nome=nome
#    self.outros = outros
#  def mostrar(self):
#    print(self.nome)
#    for sabor,preco in self.outros.items():
#      print(f'{sabor} / {preco[0]} / {preco[1]}')

#pessoa=Nome('afonso',choc=[10,5],milho=[5,7])
#pessoa.mostrar()

from datetime import datetime

class Restaurant:
  def __init__(self, restaurant_name, cuisine_type,number_served=0):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = number_served
  def decribe_restaurant(self):
    print('Nome do restaurante: {self.restaurant_name}')
    print(f'Tipo de cozinha....: {self.cuisine_type}')
    print(f'Clientes atendidos: {self.number_served}')
  def open_restaurant(self):
    print(f'O restaurnate {self.restaurant_name} está aberto!')
  def set_number_served(self,n):
    self.number_served = n
    def increment_number_served(self,n):
    self.number_served = self.number_served + n
class IceCreamStand(Restaurant):
  def __init__(self, restaurant_name, cuisine_type, *flavors):
    super().__init__(restaurant_name,cuisine_type)
    self.flavors = flavors
  def show_flavors(self):
    for i in self.flavors:
      print(i)
  def decribe_restaurant(self):
    super().decribe_restaurant()
    print(f'Sabores: {self.flavors}')
class IceCakeOnline(IceCreamStand):
  def __init__(self,restaurant_name, cuisine_type, *flavors):
    super().__init__(restaurant_name,cuisine_type, *flavors)
    self.status = 'solicitado'
    self.pedido = []
  def decribe_restaurant(self):
    super().decribe_restaurant()
    print(f'Status do pedido: {self.status}')
  def fazer_pedido(self, *flavors):
    for i in flavors:
      if i in self.flavors:
        self.pedido.append(i)
  def atender_pedido(self):
    self.status = 'atendido';
    data_pedido=datetime.now()
    hoje = data_pedido.strftime('%d/%m/%Y às %H:%M')
    print(f'Sabores dos bolos: {self.pedido}')
    arquivo = open('pedidos.txt','a')
    arquivo.write('--------PEDIDO--------\n')
    arquivo.write(hoje+'\n')
    arquivo.write('Sabores dos bolos:\n')
    for i in self.pedido:
      arquivo.write(i+'\n')
    arquivo.write('-----------------------\n')
    arquivo.close()
    print('Pedido atendido')
