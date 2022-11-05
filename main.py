##Calculadora com loop
num1 = 0.0
num2 = 0.0
oper = 0
sair = "1"
sinal = ""
##Criação da função que recebe 3 parâmetros (valores)
##E retorna 1 valor (o resultado)
def calculadora(num1,num2,oper):
  ##Se a operação é 1 realiza a soma dos números e retorna o resultado
  if(oper == "1"):
    res = num1 + num2
    return res
  ##Se a operação é 2 realiza a subtração dos números e retorna o resultado
  elif(oper == "2"):
    res = num1 - num2
    return res
  ##Se a operação é 2 realiza a multiplicação dos números e retorna o resultado
  elif(oper == "3"):
    res = num1 * num2
    return res
##Se a operação é 2 realiza a divisão dos números e retorna o resultado
  elif(oper == "4"):
    res = num1 / num2
    return res
  else:
    return 0
##Loop de repetição principal
while sair == "1":
  ##entrada de dados
  oper = input("Calculadora: Escolha a operação: (1)-Soma (2)-Subtração (3)-Multiplicação (4)-Divisão ou (0)-Sair: ")
  if(oper == "0"):
  ##Se a operação escolhida é 0 redefine a variável do loop como 0 para sair do loop e encerrar o programa
    sair = "0"
  ##Se a operação escolhida não for 1,2,3,4 dá mensagem de Opção inválida e o loop recomeça solicitando novamente a operação
  elif(oper != "1" and oper != "2" and oper != "3" and oper != "4"):
    print("Essa opção não existe")
  ##Se a operação escolhida é valida entra no Else:
  else:
    #Entrada de dados dos números da operação
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    #chama a função enviando as 3 variaveis (parametros) e imprime seu resultado
    print("Resultado:",calculadora(num1,num2,oper))
#Fora do loop o programa exibe a mensagem de programa finalizado
print("Programa Calculadora Finalizado")
