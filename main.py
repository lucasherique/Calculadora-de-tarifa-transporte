print("Tarifas de Transporte")
print("---------------------")
print("1. Estudante")
print("2. Trabalhador")
print("3. Idoso")
print("4. Comum")
print("5. Sair")

opc = (input("Escolha uma opção: "))
tarifa = 2.5

match opc:
    case "1":
        print("Você escolheu estudante!")
        q = float(input("Qual a distância percorrida em quilômetros: "))
        valor = (q * tarifa) * (50 / 100)
        valortotal = valor
    case "2":
        print("Você escolheu Trabalhador!")
        q = float(input("Qual a distância percorrida em quilômetros: "))
        valor = (q * tarifa)
        desconto = valor * (20 / 100)
        valortotal = valor - desconto
    case "3":
        print("Você escolheu Idoso!")
        q = float(input("Qual a distância percorrida em quilômetros: "))
        valortotal = 0
    case "4":
        print("Você escolheu Comum!")
        q = float(input("Qual a distância percorrida em quilômetros: "))
        valor = q * tarifa
        valortotal = valor
    case "5":
        print("Você escolheu sair.")
        valortotal = -1
    case _:

        valortotal = -1

if valortotal >= 0:
    print(f"O valor final foi de R$ {valortotal:.2f}")
elif opc == "5":
    print("FIM")
else:
    print("Você escolheu um valor inválido!")