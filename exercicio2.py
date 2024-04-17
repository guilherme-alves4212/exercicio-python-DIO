def repetir_string(texto, quantidade):

  repeticao = ""
  for _ in range(quantidade):
    repeticao += texto

  return repeticao

string_usuario = input("Digite um texto: ")  # Corrigido para 'string_usuario'
quantidade = int(input("Quantas vezes quer que o texto se repita? "))

string_repetida = repetir_string(string_usuario, quantidade)  # Corrigido para 'string_usuario'
print(f"A string '{string_usuario}' repetida {quantidade} vezes é: {string_repetida}")
