def trataTexto(texto):
    texto = texto.lower()
    caracteresInvalidos = [" ", ".", ",", "?", "!"]
    for caracter in caracteresInvalidos:
        texto = texto.replace(caracter, "")
    return texto

def verificarPalindromo(texto):
    textoTratado = trataTexto(texto)
    textoPalindromo = textoTratado[::-1]
    return textoTratado == textoPalindromo

def main():
    texto = input("Digite um texto ou palavra para verificar se é um palíndromo (exemplo: ROMA AMOR): ")

    if verificarPalindromo(texto):
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")

if __name__ == "__main__":
    main()
