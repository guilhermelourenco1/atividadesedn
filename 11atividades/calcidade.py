def mostrar_classificacao(categoria):
    print(f"De acordo com sua idade, você é classificado como: {categoria}")

entrada_idade = input("Informe sua idade (de 0 a 125 anos) para ver sua classificação: ")

try:
    idade_num = int(entrada_idade)

    if 0 <= idade_num <= 125:

        if idade_num <= 12:
            mostrar_classificacao("Criança")

        elif idade_num <= 17:
            mostrar_classificacao("Adolescente")

        elif idade_num <= 59:
            mostrar_classificacao("Adulto")

        else:
            mostrar_classificacao("Idoso")

    else:
        print("Por favor, digite uma idade válida entre 0 e 125.")

except ValueError:
    print("Erro! Só são aceitos números inteiros dentro do intervalo.")


