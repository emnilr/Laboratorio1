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
    a = float(input("Digite número (mayor que 0): "))
    
    if a <= 0:
        print("Error: el número debe ser mayor que 0.")
        return

    c = 0
    while a >= 10:
        a = a / 10
        count += 1
    print(c)
    
def potencia():










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
