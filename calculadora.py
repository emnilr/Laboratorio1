def suma(): 
    a = int(input("Digite numero: "))
    b = int(input("Digite numero: "))

    c = a + b
    print(c)
    
def resta():
    a =  int(input("Digite numero: "))
    b =  int(input("Digite numero: "))

    c = a - b
    print(c)
    
def multiplicacion():
    a =  int(input("Digite numero: "))
    b =  int(input("Digite numero: "))

    c = a * b
    print (C)
    
def division():
   a = int(input("Digite numero: "))
   b = int(input("Digite numero: "))

   c = a / b
   print(c)
def logaritmo():
    a = float(input())
    base = 10
    c = 0
    while a >= base:
        a = a / base
        c += 1
    print(c)

def potencia():
    a = float(input())
    b = float(input())
    c = a ** b
    print(c)










def main():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Logaritmo")
    print("6. Potencia ")

    opcion = input("Ingrese el numero para la función que desea realizar:")

    match opcion:
        case "1":
            suma()
        case "2":
            resta()
        case "3":
            multiplicacion()
        case "4":
            division()
        case "5":
            logaritmo()
        case "6":
            potencia()




main()
