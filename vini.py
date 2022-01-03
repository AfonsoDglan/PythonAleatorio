def Retorno(investido,taxa):
	total = (investido+(investido*taxa/100));
	for x in range(11):
		total += investido;
		total += (total*taxa/100);
	return total

resultado = Retorno(100.00,1);
print(f"soldo do investimento após 1 ano: {resultado}");

