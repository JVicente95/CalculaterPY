sair = "s"

while sair.lower() == "s":
    try:
        num1= int(input("1º numero: "))
        op = input("operador: ")
        num2 = int(input("2º numero: "))
    except Exception as ex:
         print("Valores/operdor inválidos")
         continue

    if op == "+":
        print("Resultado: ", num1 + num2)
    elif op == "-":
        print("Resultado: ", num1 - num2)
    elif op == "*" or op == "x":
        print("Resultado: ", num1 * num2)
    elif op == "/":
        print("Resultado: ", num1 / num2)
    else:
        print("Valores/operdor inválidos")

    sair = input("Continuar?s/n: ")
    
    if sair == "n":
        break