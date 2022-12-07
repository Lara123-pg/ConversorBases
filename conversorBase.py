import math

def menu():
    print('''
    1 - Decimal
    2 - Binário
    3 - Hexadecimal
    4 - Octal
    ''')

bases = ['Decimal', 'Binária', 'Hexadecimal', 'Octal']

valoresHexadecimais = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def separadorValores(valor, tam, numero, dec):
    value = ''
    num = []

    for x, y in enumerate(valor):
        value += y
        
        if len(value) == numero:
            if dec == False:
                value = value[::-1]

            num.append(value)
            value = ''

        elif tam == x and len(value) != numero:
            if numero == 3:
                if dec == False:
                    if len(value) == 1:
                        value = '00' + value
                    
                    else:
                        value = '0' + value

                else:
                    if len(value) == 1:
                        value += '00'

                    else:
                        value += '0'
            
            else:
                if dec == False:
                    if len(value) == 1:
                        value = '000' + value
                    
                    elif len(value) == 2:
                        value = '00' + value

                    else:
                        value = '0' + value

                else:
                    if len(value) == 1:
                        value += '000'

                    elif len(value) == 2:
                        value += '00'

                    else:
                        value += '0'

            num.append(value)

    return num
    
def conversorHex(valor):
    num = []
    numero = True
    valor2 = valor
    
    for x in valor:
        if str(x).isalpha():
            numero = False
    
    for x in valor2:
        letraH = False

        for key, value in valoresHexadecimais.items():
            if x != ',':
                if numero == False:
                    if str(x) == key:
                        letraH = True

                        num.append(str(value))
                    
                else:
                    if int(x) == value: 
                        letraH = True

                        num.append(str(key))
            
        if not(letraH):
            num.append(str(x))
    

    return num

def conversorBinarioFracionario(valor, num, valor2):
    binValue = []

    for x,y in enumerate(valor):
        if y != '0' and y != '1':
            valorBin = conversorDecimal(y, 'binario')
            
            if len(valorBin) < num:
                if num == 3:
                    valorBin = '0' + valorBin
                
                else:
                    valorBin = '00' + valorBin

            if x == 0:
                valorBin = str(int(valorBin))

            binValue.append(valorBin)
        
        else:
            if num == 3:
                if y == '0':
                    valorBin = '000'
                
                else:
                    valorBin = '001'
            
            else:
                if y == '0':
                    valorBin = '0000'
                
                else:
                    valorBin = '0001'
            
            if x == 0 and valor2 == True:
                valorBin = str(int(valorBin))
            
            binValue.append(valorBin)
        
    binValue = ''.join(binValue)

    return binValue

def conversorDecimalFracionario(valor, typeB, base):
    valorInt, valorDec = map(str, valor.split(','))
  
    valorConv = conversorDecimal(int(valorInt), typeB)

    valorDec2 = '0.' +str(valorDec)

    calc = 0
    result2 = ''
    result = 0
    num = []

    while True:
        value = ''
        num2 = []

        calc = float(valorDec2) * base

        if typeB == 'binario':
            valorDec2 = calc

            if calc >= 1:
                calc = str(calc)
                result2 += calc[0]

                result = str(valorConv)+','+str(result2)

                break

            else:
                calc = str(calc)
                result2 += calc[0]
        
        else:
            if calc == 0 or len(num) >= 4:
                if typeB == 'hexadecimal':
                    for x,y in enumerate(num):
                        for key, value2 in valoresHexadecimais.items():
                            if y == str(value2):
                                num[x] = str(key)
                            
                array = ''.join(num)
                result = valorConv +',' +array               

                break
            
            else:
                calc = str(calc)
                num2 = calc.split('.')

                num.append(num2[0])
                num2[0] = '0'

                for x,y in enumerate(num2):
                    if x == 1:
                        value += '.'
                    
                    value += y
                
                value = float(value)
                valorDec2 = value
    
    return result

def conversorBasesToDec(value, typeB):
    value = value[::-1]
    base = 0
    calc2 = 0

    if typeB == 'octal':
        base = 8
        
    elif typeB == 'hexadecimal':
        base = 16

        num = conversorHex(value)
    
        value = num
    
    elif typeB == 'binario':
        base = 2

    for x, y in enumerate(value):
        calc2 += int(y) * (math.pow(base, x))

    return calc2

def conversorBinarioToHexOct(valor1, typeB, num):
    lista = []

    valor1 = str(valor1)[::-1]

    valor2 = len(valor1) % num

    if valor2 != 0:
        quantidadeZeros = num - valor2

        for x in range(quantidadeZeros):
            valor1 += '0'

    result = ''

    for x in valor1:
        result += x

        valor1 = valor1.replace(x, '')


        if len(result) == num:
            calc = 0
            result2 = ''
            letra = False

            for z,y in enumerate(result):
                calc += int(y) * (2 ** z)

            if typeB == 'hexadecimal':
                for key, value in valoresHexadecimais.items():
                    if value == calc:
                        result2 += key
                        letra = True
            
            if letra == False:
                result2 += str(calc)
            
            lista.append(result2)

            result = ''
        
    r = ''.join(lista[::-1])

    return r

def conversorDecimal(value, typeB):
    result = 0
    opcao = 0

    value = int(value)

    if typeB == 'decimal':
        result = value

        return result
    
    elif typeB == 'binario':
        opcao = 2
  
    elif typeB == 'hexadecimal':
        opcao = 16
  
    elif typeB == 'octal':
        opcao = 8
    
    num = []
    conversor = value
    valor2 = False

    while value >= opcao:
        conversor2 = conversor % opcao
   
        conversor = value // opcao

        num.append(conversor2)

        if conversor < opcao:
            num.append(conversor)

        value = conversor
        valor2 = True
    
    if value < opcao and valor2 == False:
        num.append(value)

    num.reverse()
    
    result = ''

    if typeB == 'hexadecimal':
        result = conversorHex(num)
        result = ''.join(result)

    else:
        for x in num:
            result += str(x)

    return result


while True:
    print('Escolha a opção que deseja converter ou digite -1 para sair:')

    menu()

    opcaoC = int(input("Digite a opção escolhida: "))

    if opcaoC == -1:
        break

    valor = input("Qual valor deseja converter? ")

    print('Escolha para qual base quer converter o valor ou digite -1 para sair:')

    menu()

    opcaoT = int(input("Digite a opção escolhida: "))

    if opcaoT == -1:
        break
    
    # Decimal
    if opcaoC == 1:
        numero = valor
        
        #Decimal
        if opcaoT == 1:
            if ',' not in valor:
                result2 = conversorDecimal(valor, 'decimal')

            else:
                result2 = valor
            
            print(f'O valor {numero} na base {bases[0]} é {result2} na base {bases[opcaoT-1]} ')
            print('\n')
        
        #Binário
        elif opcaoT == 2:
            num = []

            if ',' not in valor:
                result = conversorDecimal(valor, 'binario')
            
            else:
                result = conversorDecimalFracionario(valor, 'binario', 2)

            print(f'O valor {numero} na base {bases[0]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')

        #Hexadecimal
        elif opcaoT == 3:
            if ',' not in valor:
                result = conversorDecimal(valor, 'hexadecimal')
            
            else:
                result = conversorDecimalFracionario(valor, 'hexadecimal', 16)
                
            print(f'O valor {numero} na base {bases[0]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')

        #Octal
        elif opcaoT == 4:
            if ',' not in valor:
                result = conversorDecimal(valor, 'octal')
            
            else:
                result = conversorDecimalFracionario(valor, 'octal', 8)
                             
            print(f'O valor {numero} na base {bases[0]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')
        
        else:
            print('A opção escolhida é inválida. Por favor, escolha um número entre 1 e 4.')
        
    #Binário
    elif opcaoC == 2:
        numero = valor

        #Decimal
        if opcaoT == 1:
            if ',' not in valor:
                result = int(conversorBasesToDec(valor, 'binario'))
            
            else:
                valorInt, valorDec = map(str, valor.split(','))

                valorBinToDec = conversorBasesToDec(valorInt, 'binario')

                calc = 0
                result = 0
                num = []

                for x in valorDec:
                    num.append(int(x))

                for x,y in enumerate(num):
                    x = x + 1
                    calc += int(y) * ((1/2)**x)

                result = valorBinToDec + calc
            
            print(f'O valor {numero} na base {bases[1]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')
        
        #Binário
        elif opcaoT == 2:
            if ',' not in valor:
                result = numero
            
            else:
                result = valor

            print(f'O valor {numero} na base {bases[1]} é {numero} na base {bases[opcaoT-1]} ')
            print('\n')

        #Hexadecimal
        elif opcaoT == 3:
            if ',' not in valor:
                result = conversorBinarioToHexOct(valor, 'hexadecimal', 4)
            
            else:
                valorInt, valorDec = map(str, valor.split(','))
                
                tamanhoStr = len(valorInt) - 1
                valorInt = valorInt[::-1]

                num = separadorValores(valorInt, tamanhoStr, 4, False)
                num.reverse()

                num.append(',')

                tamanhoStr2 = len(valorDec) - 1

                num2 = separadorValores(valorDec, tamanhoStr2, 4, True) 

                arrays = num + num2
        
                num3 = []
                for x in arrays:
                    calc = 0

                    x = x[::-1]
                    
                    if x != ',':
                        for z, y in enumerate(x):
                            calc += int(y) * (2 ** z)

                        num3.append(str(calc))
                    
                    else:
                        num3.append(',')
                
                result2 = conversorHex(num3)
                
                result = ''.join(result2)

            print(f'O valor {numero} na base {bases[1]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')
        #Octal
        elif opcaoT == 4:
            if ',' not in valor:
                result = conversorBinarioToHexOct(valor, 'octal', 3)
            
            else:
                valorInt, valorDec = map(str, valor.split(','))

                tamanhoStr = len(valorInt) - 1
                valorInt = valorInt[::-1]

                num = separadorValores(valorInt, tamanhoStr, 3, False)
                num.reverse()

                num.append(',')

                tamanhoStr2 = len(valorDec) - 1
                num2 = separadorValores(valorDec, tamanhoStr2, 3, True) 

                arrays = num + num2
    
                num3 = []

                for x in arrays:
                    calc = 0
       
                    x = x[::-1]
                    
                    if x != ',':
                        for z, y in enumerate(x):
                            calc += int(y) * (2 ** z)

                        num3.append(str(calc))
                    
                    else:
                        num3.append(',')
                
                result = ''.join(num3)

            print(f'O valor {numero} na base {bases[1]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')
            
        else:
            print('A opção escolhida é inválida. Por favor, escolha um número entre 1 e 4.')
    
    #Hexadecimal
    elif opcaoC == 3:
        numero = valor

        #Decimal
        if opcaoT == 1:
            if ',' not in valor:
                result = int(conversorBasesToDec(valor, 'hexadecimal'))
            
            else:
                valorInt, valorDec = map(str, valor.split(','))

                hexToDec = int(conversorBasesToDec(valorInt, 'hexadecimal'))
                
                calc = 0
                result = 0
                num = []

                num = conversorHex(valorDec)

                for x,y in enumerate(num):
                    x = x + 1
                    calc += int(y) * ((1/16)**x)

                
                result = hexToDec + calc
            
            print(f'O valor {numero} na base {bases[2]} é {result} na base {bases[opcaoT-1]} ')
            print('\n') 
        
        #Binário
        elif opcaoT == 2:
            if ',' not in valor:
                result2 = conversorBasesToDec(valor, 'hexadecimal')
                result = conversorDecimal(result2, 'binario')  
            
            else:
                num = []

                num = conversorHex(valor)
                valorInt = []
                valorDec = []

                indexV = num.index(',')

                for x,y in enumerate(num):
                    if x < indexV:
                        valorInt.append(y)
                    
                    else:
                        if y != ',':
                            valorDec.append(y)

                
                valorIntB = conversorBinarioFracionario(valorInt, 4, True)
                valorDecB = conversorBinarioFracionario(valorDec, 4, False)

                result = valorIntB +',' +valorDecB
               
            print(f'O valor {numero} na base {bases[2]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')

        #Hexadecimal
        elif opcaoT == 3:
            if ',' not in valor:
                result = numero
            
            else:
                result = valor

            print(f'O valor {numero} na base {bases[2]} é {numero} na base {bases[opcaoT-1]} ')
            print('\n') 
        
        #Octal
        elif opcaoT == 4:
            if ',' not in valor:
                result2 = conversorBasesToDec(valor, 'hexadecimal')
                result = conversorDecimal(result2, 'octal')
            
            else:
                valorInt, valorDec = map(str, valor.split(','))

                hexToDec = conversorBasesToDec(valorInt, 'hexadecimal')
                
                calc = 0
                result = 0
                num = []

                num = conversorHex(valorDec)
            
                for x,y in enumerate(num):
                    x = x + 1
         
                    calc += int(y) * ((1/16)**x)
                  
                result2 = hexToDec + calc

                result2 = str(result2).replace('.', ',')
          
                result = conversorDecimalFracionario(result2, 'octal', 8)
        
            print(f'O valor {numero} na base {bases[2]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')
               
        else:
            print('A opção escolhida é inválida. Por favor, escolha um número entre 1 e 4.')
        
    #Octal
    elif opcaoC == 4:
        numero = valor
        
        #Decimal
        if opcaoT == 1:
            if ',' not in valor:    
                result = int(conversorBasesToDec(valor, 'octal'))
            
            else:
                num = []

                valorInt, valorDec = map(str, valor.split(','))
      
                result2 = conversorBasesToDec(valorInt, 'octal')

                for x in valorDec:
                    num.append(int(x))
                
                calc = 0

                for x,y in enumerate(num):
                    x = x + 1
                    calc += int(y) * ((1/8)**x)

                result = result2 + calc
            
            print(f'O valor {numero} na base {bases[3]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')
        
        #Binário
        elif opcaoT == 2:
            if ',' not in valor:
                result2 = conversorBasesToDec(valor, 'octal')
                result = conversorDecimal(result2, 'binario')
            
            else:
                valorInt, valorDec = map(str, valor.split(','))

                binInt = conversorBinarioFracionario(valorInt, 3, True)
                binInt = int(binInt)
            
                binDec = conversorBinarioFracionario(valorDec, 3, False)

                
                result = str(binInt) +',' +binDec     

            print(f'O valor {numero} na base {bases[3]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')
        
        #Hexadecimal
        elif opcaoT == 3:
            if ',' not in valor:
                result2 =  conversorBasesToDec(valor, 'octal')
                result = conversorDecimal(result2, 'hexadecimal')

            else:
                num = []

                valorInt, valorDec = map(str, valor.split(','))
      
                result2 = conversorBasesToDec(valorInt, 'octal')

                for x in valorDec:
                    num.append(int(x))
                
                calc = 0

                for x,y in enumerate(num):
                    x = x + 1
                    calc += int(y) * ((1/8)**x)

                result3 = result2 + calc
                
                result4 = str(result3).replace('.', ',')
           
                result = conversorDecimalFracionario(result4, 'hexadecimal', 16)
          
            print(f'O valor {numero} na base {bases[3]} é {result} na base {bases[opcaoT-1]} ')
            print('\n')

        #Octal
        elif opcaoT == 4:
            if ',' not in valor:
                result = numero
            
            else:
                result = valor

            print(f'O valor {numero} na base {bases[3]} é {numero} na base {bases[opcaoT-1]} ')
            print('\n')
        
        else:
            print('A opção escolhida é inválida. Por favor, escolha um número entre 1 e 4.')
    
    else:
        print('A opção escolhida é inválida. Por favor, escolha um número entre 1 e 4.')