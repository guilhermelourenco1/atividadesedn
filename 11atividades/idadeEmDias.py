def eh_ano_bissexto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

def calcula_idade_em_dias(ano_nasc, ano_atual):
    anos_bissextos = []
    total_dias = 0

    for ano in range(ano_nasc, ano_atual + 1):
        if eh_ano_bissexto(ano):
            total_dias += 366
            anos_bissextos.append(ano)
        else:
            total_dias += 365

    return total_dias, anos_bissextos

def iniciar():
    ano_atual = 2025  

    while True:
        entrada = input("Informe seu ano de nascimento (ou digite 'sair' para encerrar): ").strip().lower()

        if entrada == 'sair':
            print("Finalizando o programa. Até mais!")
            break

        try:
            ano_nascimento = int(entrada)

            if ano_nascimento < 0:
                print("Ano inválido! Não aceite números negativos.")
                continue

            if ano_nascimento > ano_atual:
                print(f"Ano inválido! O ano de nascimento não pode ser maior que {ano_atual}.")
                continue

            dias_vividos, anos_bissextos = calcula_idade_em_dias(ano_nascimento, ano_atual)
            print(f"Sua idade aproximada em dias é: {dias_vividos}")
            print(f"Anos bissextos vividos: {anos_bissextos}")

        except ValueError:
            print("Por favor, informe um número inteiro válido para o ano.")

if __name__ == "__main__":
    iniciar()
