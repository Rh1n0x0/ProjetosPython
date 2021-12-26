def cifra(strings,numero):
    if numero > 25:
        return print('Escolha o numero de rotações sendo ele entre 1 e 25.')
    for letras in strings:
       letra_convertida = ord(str(letras))

       if letra_convertida > 64 and letra_convertida < 91:
            if letra_convertida + numero > 90:
                letra_para_printar = 64 + numero
                print(chr(letra_para_printar),end='')
            elif letra_convertida < 91:
                letra_para_printar = letra_convertida + numero
                print(chr(letra_para_printar),end='')
       elif letra_convertida > 96 and letra_convertida < 123:
            if letra_convertida + numero > 122:
                letra_para_printar = 96 + numero
                print(chr(letra_para_printar),end='')
            elif letra_convertida < 123:
                letra_para_printar = letra_convertida + numero
                print(chr(letra_para_printar),end='')

    print("\nConteúdo antes da conversão: ", strings)


letras_para_converter = input('Digite o conteúdo que quer converter para Cifra de César: ')
numero_de_rotacao = int(input('Digite quantas rotações devem ser feitas(o limite é 25): '))

cifra(letras_para_converter,numero_de_rotacao)
