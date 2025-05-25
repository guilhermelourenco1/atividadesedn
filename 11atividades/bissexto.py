def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def rodar_verificacao():
    entrada = input("Informe um ano para verificar se é bissexto (exemplo: 1996): ")

    try:
        ano_informado = int(entrada)

        if eh_bissexto(ano_informado):
            print(f"O ano {ano_informado} é um ano bissexto!")
        else:
            print(f"O ano {ano_informado} NÃO é bissexto!")

    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros válidos.")

if __name__ == "__main__":
    rodar_verificacao()
