def mostrar_imc(valor_imc):
    print(f"Seu índice de massa corporal (IMC) é: {valor_imc:.2f}")

def avaliar_imc(valor_imc):
    if valor_imc <= 18.5:
        print("Cuidado! Você está abaixo do peso ideal.")
        mostrar_imc(valor_imc)
        return

    if valor_imc <= 24.9:
        print("Ótimo! Seu peso está dentro do normal.")
        mostrar_imc(valor_imc)
        return

    if valor_imc <= 29.9:
        print("Atenção! Você está com sobrepeso.")
        mostrar_imc(valor_imc)
        return

    if valor_imc <= 34.9:
        print("Atenção! Obesidade grau I detectada.")
        mostrar_imc(valor_imc)
        return

    if valor_imc <= 39.9:
        print("Atenção! Obesidade grau II detectada.")
        mostrar_imc(valor_imc)
        return

    print("Atenção! Obesidade grau III detectada.")
    mostrar_imc(valor_imc)

def executar():
    peso_input = input("Digite seu peso em Kg (ex: 70.2): ")
    altura_input = input("Digite sua altura em metros (ex: 1.75): ")

    try:
        peso_valor = float(peso_input)
        altura_valor = float(altura_input)
        imc_calculado = peso_valor / (altura_valor ** 2)
        avaliar_imc(imc_calculado)

    except ValueError:
        print("Por favor, informe apenas números válidos usando ponto para decimais.")

if __name__ == "__main__":
    executar()
