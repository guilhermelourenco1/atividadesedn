def mensagem_erro(entidade):
    print(f"Opa! Valor inválido para {entidade}.")
    print("Digite apenas números, use ponto para decimais. Tente de novo!\n")


def pedir_float(mensagem, entidade):
    while True:
        valor = input(mensagem)
        try:
            return float(valor)
        except ValueError:
            mensagem_erro(entidade)


print("Calculadora de Gorjeta\n")

valor_comanda = pedir_float("Informe o valor total da comanda: R$ ", "comanda")
percentual_gorjeta = pedir_float("Informe o percentual da gorjeta (%): ", "gorjeta")

valor_gorjeta = valor_comanda * (percentual_gorjeta / 100)
total_com_gorjeta = valor_comanda + valor_gorjeta

print(f"\nA gorjeta será: R$ {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {total_com_gorjeta:.2f}")
print("\nObrigado por usar a calculadora!")
