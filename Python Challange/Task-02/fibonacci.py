def fibonacci(numero):
    if numero < 0:
        return False

    a, b = 0, 1
    
    if numero == a or numero == b:
        return True

    while b < numero:
        a, b = b, a + b
        if b == numero:
            return True

    return False

numero = int(input("Digite um numero: "))

if fibonacci(numero):
    print(f"O numero pertence a sequência de Fibonacci.")
else:
    print(f"O numero nao pertence a sequência de Fibonacci.")

