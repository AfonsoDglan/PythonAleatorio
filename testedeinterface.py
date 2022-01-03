from tkinter import *
# função que será executada quando o botão for pressionado
def Evento():
	resultado['text']= entrada.get()
	resultado['fg']='red'
# instânciando uma janela vazia
container = Tk()
#título da janela
container.title('IceCake')
#dimentões da janela
container.geometry('400x300')
#elemento texto inserido na janela
texto=Label(container,text='Loja de bolos')
#empacotando o elemento texto na janela
texto.pack()
#elemento botão inserido na janela
botao=Button(container,text='Clica aqui', command=Evento)
#empacotando o elemento botão na janela
botao.pack()
#elemento entrada de dados inserido na janela
entrada=Entry(container)
#empacotando o elemento entrada de dados
entrada.pack()
#elemento texto inserido na janela
resultado=Label(container,text='RESULTADO', fg='blue')
#empacotando o elemento texto na janela
resultado.pack()
#executando a janela (event loop)
container.mainloop()
