import os
os.system("cls||clear")

primeiroNumero = int(input("Digite o 1º número: "))
segundoNumero  = int(input("Digite o 2º número: "))

maiorValor = max(primeiroNumero, segundoNumero)
menorValor = min(primeiroNumero, segundoNumero)
soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero
media = soma / 2
   

print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Menor valor: {menorValor}")
print(f"Maior valor: {maiorValor}")