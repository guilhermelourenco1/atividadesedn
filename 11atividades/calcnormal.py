def executar_operacao(num1, num2, op):
    if op == '+':
        res = num1 + num2
        return f"Soma: {res:.2f}"
    elif op == '-':
        res = num1 - num2
        return f"Subtração: {res:.2f}"
    elif op == '*':
        res = num1 * num2
        return f"Multiplicação: {res:.2f}"
    elif op == '/':
        if num2 == 0:
            return "Erro: divisão por zero não permitida."
        else:
            res = num1 / num2
            return f"Divisão: {res:.2f}"
    else:
        return "Operação desconhecida."

def iniciar_calculadora():
    while True:
        entrada1 = input("Informe o primeiro número: ")
        entrada2 = input("Informe o segundo número: ")

        try:
            entrada1 = float(entrada1)
            entrada2 = float(entrada2)
        except ValueError:
            print("Erro: apenas números são aceitos. Use ponto para decimais.")
            continue

        while True:
            operador = input("Digite o operador (+, -, *, /): ")
            if operador in ['+', '-', '*', '/']:
                resultado = executar_operacao(entrada1, entrada2, operador)
                print(resultado)
                return
            else:
                print("Operador inválido! Use somente +, -, * ou /.")

iniciar_calculadora()
