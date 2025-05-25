def validar_senha(senha):
    if len(senha) < 8:
        print("A senha precisa conter no mínimo 8 caracteres.")
        return False

    if not any(char.isdigit() for char in senha):
        print("A senha deve incluir ao menos um número.")
        return False

    return True

def executar_verificacao():
    while True:
        entrada = input("Por favor, insira sua senha para avaliação (ou digite 'sair' para encerrar): ").strip()

        if entrada.lower() == 'sair':
            print("Encerrando o programa. Obrigado!")
            break

        if validar_senha(entrada):
            print("Senha válida e considerada segura.")
            print(f"Senha informada: {entrada}")
            break

if __name__ == "__main__":
    executar_verificacao()
