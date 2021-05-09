import turtle


tess = turtle.Turtle()


def triangle(x, y):
    """Função para desenhar triangulos apartir de um click do mouse"""

    # Levando o pincel para a posição x, y sem desenhar nada
    tess.penup()
    tess.goto(x, y)  # Posição recebida através do método onscreenclick
    tess.pendown()

    for i in range(3):
        # Desenhar o Triangulo partindo do click
        tess.forward(100)
        tess.left(120)
        tess.forward(100)


# Metodo que passa como argumento para uma função as cordenadas (x,y) de um click, nesse caso a função triangle
turtle.onscreenclick(triangle, 1)

turtle.listen()
turtle.done()
