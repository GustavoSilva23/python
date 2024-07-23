def decimal_para_binario(decimal):
    try:
        decimal = int(decimal)
    except ValueError:
        print("Valor inválido. Digite um número decimal")
        return None
    
    binario = bin(decimal)[2:]
    return binario

def decimal_para_hexadecimal(decimal):
    try:
        decimal = int(decimal)
    except ValueError:
        print("Valor inválido. Digite um número decimal")
        return None
    
    hexadecimal = hex(decimal)[2:]
    return hexadecimal

def decimal_para_octal(decimal):
    try:
        decimal = int(decimal)
    except ValueError:
        print("Valor inválido. Digite um número decimal")
        return None
    
    octal = oct(decimal)[2:]
    return octal

decimal = input("Digite um número decimal: ")
binario = decimal_para_binario(decimal)
hexadecimal = decimal_para_hexadecimal(decimal)
octal = decimal_para_octal(decimal)

if binario is not None and hexadecimal is not None and octal is not None:
    print("O número binário equivalente é:", binario)
    print("O número hexadecimal equivalente é:", hexadecimal)
    print("O número octal equivalente é:", octal)
