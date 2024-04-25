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

