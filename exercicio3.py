primeiroNum = int(input("Qual o primeiro numero? "))
segundoNum = int(input("Qual o segundo numero? "))
operacao = (input("Qual operaçao matemática voce deseja? (soma // subtracao // divisao // multiplicacao)"))

if operacao == "soma":
    print("A operação escolhida foi soma, portanto: ", primeiroNum + segundoNum)
elif operacao == "subtracao":
    print("A operação escolhida foi subtracao, portanto: ", primeiroNum - segundoNum)
elif operacao == "divisao":
    print("A operação escolhida foi divisao, portanto: ", primeiroNum / segundoNum)
elif operacao == "multiplicacao":
    print("A operação escolhida foi multiplicacao, portanto: ", primeiroNum * segundoNum)
else:
    print("Escolha um operador válido!")