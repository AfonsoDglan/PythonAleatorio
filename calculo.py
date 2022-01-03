n1 = 0;
for x in range(1,11):
	lista=float(input("Digite a nota da %d° lista:"%x));
	n1 += lista;
n2 = float(input("digite a nota da primeira prova: "));
n3 = float(input("digite a nota da segunda prova: "));
print(n1);
notaFim = ((4*n1)+(3*n2)+(3*n3))/10;
print(f"A nota final é: ",notaFim);

