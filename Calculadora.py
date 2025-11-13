def main():
    print("Calculadora Simple")
    print("Operaciones disponibles: +, -, *, /")
    
    try:
        num1 = float(input("Ingresa el primer número: "))
        operacion = input("Ingresa la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
                return
            resultado = num1 / num2
        else:
            print("Operación no válida.")
            return
        
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingresa números válidos.")

if __name__ == "__main__":
    main()

