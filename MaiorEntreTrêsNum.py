print("- MAIOR ENTRE TRÊS NÙMEROS -\n")
a = int(input("Insira um número: "))
b = int(input("Insira um número: "))
c = int(input("Insira um número: "))

maior = a

if b > maior:
  maior = b
if c > maior:
    maior = c
print("Maior: ", maior )
