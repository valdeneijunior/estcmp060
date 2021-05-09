import turtle
from math import pi as PI  # Importando PI


def fractal_fibo(n):
    """Função para desenhar o fractal e a espiral de fibonacci"""

    # Inicializando a sequencia de fibonacci
    # Para os quadrados e para a espiral
    spiral_a = 0
    spiral_b = 1
    square_a = spiral_a
    square_b = spiral_b

    # Configurar a cor das linhas dos quadrados
    x.pencolor("blue")

    # Desenhar o primeiro quadrado
    x.forward(square_b * factor)
    x.left(90)
    x.forward(square_b * factor)
    x.left(90)
    x.forward(square_b * factor)
    x.left(90)
    x.forward(square_b * factor)

    # Seguindo com a sequencia de fibonacci para os quadrados
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Desenhar o resto dos quadrados
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # Seguindo com a sequencia de fibonacci para os quadrados
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Levar o pincel para o inicio da espiral
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Configurando a cor da espiral
    x.pencolor("red")

    # Desenhar a espiral de fibonacci
    # Printar a sequencia de n numeros de fibonacci no terminal
    x.left(90)
    for i in range(n):
        print(spiral_b)
        fdwd = PI * spiral_b * factor / 2
        fdwd /= 90

        for j in range(90):
            x.forward(fdwd)
            x.left(1)

        # Seguindo com a sequencia de fibonacci
        temp = spiral_a
        spiral_a = spiral_b
        spiral_b = temp + spiral_b


factor = 1  # Fator de configuração da escala dos quadrados

# Receber a quantidade de numeros de fibonacci
quant_fib = int(input('Enter the number of iterations (must be > 1): '))

# Checar se o numero recebido é diferente de zero(0)
# Plotar o fractal e a spiral de fibonacci
if quant_fib > 0:
    print("Fibonacci series for", quant_fib, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fractal_fibo(quant_fib)
    turtle.done()
else:
    print("Number of iterations must be > 0")
