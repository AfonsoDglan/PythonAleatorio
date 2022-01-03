lista = [];
while True:
	a =  int(input(""));
	if(a == -1):break
	else:
		lista.append(a)
media = sum(lista)/len(lista)
soma = 0;
for x in range(len(lista)):
	soma += (lista[x] - media)**2;
print(f"media: {media}");
print(f"soma: {soma}");
s = sum(lista);
print(f"soma da lista: {s}")
