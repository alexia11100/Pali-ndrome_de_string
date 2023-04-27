#Palíndrome
#Para verificar de a string pode ser lida de tras para frente

string = input("Digite uma palavra: ")
reverce_string = string[::-1]

if string == reverce_string:
    print("É Políndrome!")

else: 
    print("Não é Políndrome!")