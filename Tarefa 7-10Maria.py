#6-
import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio ** 2)

print(f"A área do círculo com raio {raio} é: {area}")

#7
numero1 = float(input("primeiro número: "))
numero2 = float(input("segundo número: "))
numero3 = float(input("terceiro número: "))

media = (numero1 + numero2 + numero3) / 3

print(f"A média dos números {numero1}, {numero2} e {numero3} é: {media}")

#8
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+ para soma, - para subtração, * para multiplicação, / para divisão): ")


if operacao == '+':
    resultado = soma(numero1, numero2)
elif operacao == '-':
    resultado = subtracao(numero1, numero2)
elif operacao == '*':
    resultado = multiplicacao(numero1, numero2)
elif operacao == '/':
    resultado = divisao(numero1, numero2)
else:
    resultado = "Operação inválida."


print(f"O resultado da operação é: {resultado}")

#9
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!Vai se fuder!")

#10
numero = float(input("Digite um número: "))

quadrado = numero ** 2
triplo = numero * 3

print(f"O quadrado de {numero} é: {quadrado}")
print(f"O triplo de {numero} é: {triplo}")
