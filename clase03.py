def suma(numero1, numero2):
    print(numero1 + numero2)


def resta(numero1, numero2):
    print(numero1 - numero2)

def tipo(tipo, numero1 , numero2):
    if tipo == 1:
        suma(numero1,numero2)
    else:
        resta(numero1 , numero2)
        
if __name__ == '__main__':
    numero1 = int(input("Ingresar primer numero: "))
    numero2 = int (input("Ingresa segundo numero: "))
    r = int(input("Elija que operacion quiere realizar: 1)Suma        2)Resta :"))
    tipo(r, numero1, numero2)





