def mostrar_relatorio(lista_pares, lista_impares):
    qtd_pares = len(lista_pares)
    qtd_impares = len(lista_impares)
    total = qtd_pares + qtd_impares

    print("Você optou por encerrar. Aqui está o resumo dos números digitados:")
    print(f"\nQuantidade de números pares: {qtd_pares}")
    print(f"Quantidade de números ímpares: {qtd_impares}")
    print(f"Total de números fornecidos: {total}")

def executar():
    numeros_pares = []
    numeros_impares = []

    while True:
        entrada_usuario = input("Informe um número inteiro para verificar par ou ímpar, ou 'sair' para finalizar: ").strip()

        if entrada_usuario.lower() == 'sair':
            mostrar_relatorio(numeros_pares, numeros_impares)
            print("\nEncerrando o programa. Até logo!")
            break

        try:
            numero = int(entrada_usuario)
            if numero % 2 == 0:
                numeros_pares.append(numero)
                print(f"{numero} é um número par.")
            else:
                numeros_impares.append(numero)
                print(f"{numero} é um número ímpar.")
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros válidos.")

if __name__ == "__main__":
    executar()
