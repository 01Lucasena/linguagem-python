import os
os.system("cls||clear")

quilosMaca = float(input("Digite a quantidade de Maçãs(Kg): "))
quilosMorango = float(input("Digite a quantidade de Morangos(Kg): "))
quilosTotal = quilosMaca + quilosMorango

"""
 morango 2,50 //+5kg 2,20
 maçã 1,80 //+5kg 1,50
                        """  
if quilosMaca <= 5:
    precoMaca = quilosMaca * 1.80

else:
    precoMaca = quilosMaca * 1.50

if quilosMorango <= 5:
    precoMorango = quilosMorango * 2.50

else:
    precoMorango = quilosMorango * 2.20    

valorTotal = precoMaca + precoMorango

print(f"Quantidade de maçãs: {quilosMaca}")
print(f"Quantidade de morangos: {quilosMorango}")
print(f"Preço das maçãs: {precoMaca}")
print(f"Preço dos morangos: {precoMorango}")

if quilosTotal > 8 or valorTotal > 25:
    desconto10 = valorTotal * 0.10
    valorComDesconto = valorTotal - desconto10
    print(f"Valor Total: {valorTotal}")
    print(f"Desconto: {desconto10}")
    print(f"Valor Total com desconto : {valorComDesconto}")

else:
    print(f"Valor Total: {valorTotal}")