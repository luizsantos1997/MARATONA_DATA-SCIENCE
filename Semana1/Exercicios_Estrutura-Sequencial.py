import math
# Author: Luiz Eduardo for Data-Science Marathon
# https://wiki.python.org.br/EstruturaSequencial
# 1 - Exercicio
print("Olá Mundo")

# 2 - Exercicio
saida = int(input("Insira um número"))
print(saida)

#3 - Exercicio
a = int(input("Digite um número"))
b = int(input("Digite um número"))
print(a+b)

#4 - Exercicio
c = 0
for i in range(2):
    for z in range(4):

        c = c + int(input("Digite a nota da prova " +
                          str(z+1)+" do bimestre "+str(i+1)+":"))
c = c/8
print(c)

#5 - Exercicio
meterToCentime = float(input("Valor em metros"))
meterToCentime *= 100
print(str(meterToCentime)+" Centimetros")

#6 Exercicio
raio = float(input("Digite o raio do circulo"))
raio = raio ** 2
raio = 3.14 * raio
print(raio)

#7 Exercicio
lado = float(input("Digite o lado do quadrado"))
lado *= lado
lado *= 2
print(lado)

#8 Exercicio
valorPorHora = float(input("Digite o valor de uma horas"))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas"))
salario = valorPorHora * horasTrabalhadas
print("Salário total no mês:R${0:.2f}".format(salario))

#9 Exercicio
farenheint = float(input("Temperatura em Farenheit:"))
celsius = (5 *(farenheint -32)/9)
print(celsius)

#10 Exercicio
celsius = float(input("Temperatura em Farenheit:"))
farenheint = (celsius * 9/5) + 32
print(farenheint)

#11 Exercicio
inteiro1 = int(input("Digite um inteiro:"))
inteiro2 = int(input("Digite um inteiro:"))
real = float(input("Digite um real:"))
print("{primeiro} ".format(primeiro=(2*(inteiro1*2) * (inteiro2/2) )))
print("{segundo}".format(segundo=(inteiro1*3)+real))
print("{terceiro}".format(terceiro=(real**3)))

#12 Exercicio
altura = float(input("Digite altura"))
altura = (72.7*altura) - 58
print(altura)

#13 Exercicio
altura = float(input("Digite altura"))
print("Peso ideal para homem:{homem}\nPeso ideal para Mulher:{mulher}.".format(homem=(72.7*altura) - 58,mulher=(62.1*altura) - 44.7))

#14 Exercicio
pesoPeixe = float(input("Insira Peso do Peixe:"))
if pesoPeixe <= 50:
        print("Peso aceitável, sem multa a pagar")
elif pesoPeixe > 50:
        print("Peso elevado em {peso:.3f} Kilos,Multa de {multa:.2f}".format(peso=(pesoPeixe % 50),multa=4*(pesoPeixe % 50)))


#15 Exercicio
valorPorHora = float(input("Digite o valor de uma horas"))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas"))
print("Salario Total:{salario}".format(salario=valorPorHora*horasTrabalhadas))
print("Imposto de Renda:{IR}".format(IR=(valorPorHora*horasTrabalhadas)*0.11))
print("INSS:{INSS}".format(INSS=(valorPorHora*horasTrabalhadas)*0.08))
print("Sindicato:{Sindicato}".format(Sindicato=(valorPorHora*horasTrabalhadas)*0.05))
print("Salario Total:{Liquido}".format(Liquido=valorPorHora*horasTrabalhadas-(valorPorHora*horasTrabalhadas*(0.11+0.05+0.08))))

#16 Exercicio
qtdMetroPintar = float(input("Quantos metros irá pagar:"))
qtdLatas = math.ceil((qtdMetroPintar/3)/18)
print("Serão necessário {latas} com total de:R${preco:.2f}".format(latas=qtdLatas,preco=(qtdLatas*80.00)))