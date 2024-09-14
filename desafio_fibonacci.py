def pertence_fibonacci(n):
    # Iniciando os primeiros números da sequência
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    
    # Verifica se o número é igual a um dos números da sequência
    if b == n or n == 0:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Defina o número aqui
numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))
