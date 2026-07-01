# ==========================================
# PROJETO: CALCULADORA COM HISTÓRICO
# ==========================================

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "ERRO: Impossível dividir por zero"
    return n1 / n2

def calcular(opcao, n1, n2):
# Gerencia qual operação matemática será executada
    if opcao == '+':
        return soma(n1, n2)
    elif opcao == '-':
        return subtracao(n1, n2)
    elif opcao == '*':
        return multiplicacao(n1, n2)
    elif opcao == '/':
        return divisao(n1, n2)

def obter_numeros():
# Validar a entrada do usuário para garantir que apenas números serão aceitos
    while True:
        try:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            return n1, n2
        except ValueError:
            print('Erro de sintaxe! Digite apenas números válidos\n')

# ----------------
# FLUXO PRINCIPAL
# ----------------
historico = []

while True:
    print('\n Calculadora \n'
          '+ - Soma\n'
          '- - Subtração\n'
          '* - Multiplicação\n'
          '/ - Divisão\n'
          '1 - Histórico de operação\n'
          '0 - Sair\n')

    escolha = input('Digite o tipo de operação: ').strip()

    if escolha == '0':
        print('Até a próxima!')
        break

    elif escolha == '1':
        if len(historico) == 0:
            print('Nenhuma operação realizada')
        else:
            print('\n=== Histórico ===')
            for operacao in historico:
                print(operacao)
        continue

    elif escolha not in ['+', '-', '*', '/']:
        print('Operação inválida! Escolha uma opção do menu')
        continue

    # Execução dos Cálculos
    num1, num2 = obter_numeros()
    resultado = calcular(escolha, num1, num2)

    print(f'\nResultado: {resultado}')
    historico.append(f'{num1} {escolha} {num2} = {resultado}')
