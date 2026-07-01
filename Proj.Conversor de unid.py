# Conversor de unidades em Python
# Projeto de estudo - funções, loops e organização de código
def ler_float(opcao):
    return float(input(opcao))

def ler_int(valor):
    return int(input(valor))

def comprimento():
    print("\n1 - Metros -> Quilômetros \n"
          "2 - Quilômetros -> Metros \n"
          "3 - Metros -> Centímetros \n"
          "4 - Centímetros -> Metros \n"
          "0 - Voltar \n")

    def metros_km(valor):
        return valor / 1000

    def km_metros(valor):
        return valor * 1000

    def metros_cent(valor):
        return valor / 100

    def cent_metros(valor):
        return valor * 100

    while True:
        escolha = ler_int("Escolha uma opção: ")
        if escolha == 0:
            return
        n1 = ler_float("Digite um valor: ")

        if escolha == 1:
            resultado = metros_km(n1)
            print(f'{resultado}Km')

        elif escolha == 2:
            resultado = km_metros(n1)
            print(f"{resultado}M")

        elif escolha == 3:
            resultado = metros_cent(n1)
            print(f"{resultado}CM")

        elif escolha == 4:
            resultado = cent_metros(n1)
            print(f"{resultado}M")

        else:
            print("Opção Inválida")

def massa():
    print("\n1 - Toneladas -> Kg \n"
          "2 - Kg -> Toneladas\n"
          "3 - Kg -> gramas\n"
          "4 - Gramas -> Kg\n"
          "0 - Voltar \n")

    def tone_kg(valor):
        return valor * 1000

    def kg_tone(valor):
        return valor / 1000

    def kg_gramas(valor):
        return valor * 1000

    def gramas_kg(valor):
        return valor / 1000

    while True:
        escolha = ler_float("Escolha uma opção: ")
        if escolha == 0:
            return
        n1 = ler_float("Digite um valor: ")

        if escolha == 1:
            resultado = tone_kg(n1)
            print(f"{resultado}Kg")

        elif escolha == 2:
            resultado = kg_tone(n1)
            print(f"{resultado}T")

        elif escolha == 3:
            resultado = kg_gramas(n1)
            print(f"{resultado}g")

        elif escolha == 4:
            resultado = gramas_kg(n1)
            print(f"{resultado}Kg")

        else:
            print("Opção Inválida")

def temperatura():
    print("\n1 - Celsius -> Fahrenheit \n"
          "2 - Fahrenheit -> Celsius\n"
          "3 - Celsius -> Kelvin \n"
          "4 - Kelvin -> Celsius \n"
          "5 - Kelvin -> Fahrenheit \n"
          "6 - Fahrenheit -> Kelvin\n"
          "0 - Voltar \n")

    def cel_fah(valor):
        return (valor * 1.8) + 32
    def fah_cel(valor):
        return (valor - 32) / 1.8
    def cel_k(valor):
        return valor + 273.15
    def k_cel(valor):
        return valor - 273.15
    def k_fah(valor):
        return (valor - 32) /1.8 + 273.15
    def fah_k(valor):
        return (valor - 273.15) * 1.8 + 32


    while True:
        escolha = ler_int("Escolha uma opção: ")
        if escolha == 0:
            return

        if escolha == 1:
            temp = ler_float("Digite a temperatura em Celsius : ")
            resultado = cel_fah(temp)
            print(f"{resultado}ºF")

        elif escolha == 2:
            temp = ler_float("Digite a temperatura em Fahrenheit : ")
            resultado = fah_cel(temp)
            print(f"{resultado}ºC")

        elif escolha == 3:
            temp = ler_float("Digite a temperatura em Celsius : ")
            resultado = cel_k(temp)
            print(f"{resultado}K")

        elif escolha == 4:
            temp = ler_float("Digite a temperatura em Kelvin : ")
            resultado = k_cel(temp)
            print(f"{resultado}ºC")

        elif escolha == 5:
            temp = ler_float("Digite a temperatura em Kelvin : ")
            resultado = k_fah(temp)
            print(f"{resultado}ºF")

        elif escolha == 6:
            temp = ler_float("Digite a temperatura em Fahrenheit : ")
            resultado = fah_k(temp)
            print(f"{resultado}K")

        else:
            print("Opção Inválida")

def menu():
    while True:
        print("CONVERSOR DE UNIDADES")
        print("1 -> Comprimento")
        print("2 -> Massa")
        print("3 -> Temperatura")
        print("0 - Sair")

        escolha = ler_int("Escolha uma opção: ")
        if escolha == 1:
            comprimento()
        elif escolha == 2:
            massa()
        elif escolha == 3:
            temperatura()
        elif escolha == 0:
            print("Encerrando o programa")
            break

menu()