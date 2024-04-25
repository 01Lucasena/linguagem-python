import os
os.system("cls||clear")

nomeProduto = input("Digite o nome do produto: ")
quantidadeAdquirida = int(input("Digite a quantidade adquirida: "))
precoUnitario = float(input("Digite o preço do produto: "))

total = quantidadeAdquirida * precoUnitario

if quantidadeAdquirida <= 5:
    desconto =  total * 0.02

elif quantidadeAdquirida > 5 and quantidadeAdquirida <= 10:
    desconto = total * 0.03

else:
    desconto = total * 0.05

totalAPagar = total - desconto

print(f"Total: {total}")
print(f"Desconto: {desconto}")
print(f"Total a pagar: {totalAPagar}")