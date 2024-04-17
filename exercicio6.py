def verifica_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return True
    else:
        return False

palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

if verifica_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")