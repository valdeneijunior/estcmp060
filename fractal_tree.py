from turtle import *


speed('fastest')


lt(90)

# Configurando o angulo dos ramos
angle = 30


def fractal_tree(sz, level):
    """ Função para plotar uma arvore fractal de tamanho sz com n levels"""

    if level > 0:
        colormode(255)

        # Configurando a cor de cada nivel
        pencolor(0, 255 // level, 0)

        fd(sz)

        rt(angle)

        # Chamada recursiva para os ramos do lado direito
        fractal_tree(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        lt(2 * angle)

        # Chamada recursiva para os ramos do lado esquerdo
        fractal_tree(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)


# Chamada para a função desenhar um fractal de tamanho 80 com 7 niveis
fractal_tree(80, 7)

done()
