from turtle import *

def courbe_von_koch(n, L):
    if n == 0:
        forward(L)
    else:
        courbe_von_koch(n-1, L/3)
        left(60)
        courbe_von_koch(n-1, L/3)
        right(120)
        courbe_von_koch(n-1, L/3)
        left(60)
        courbe_von_koch(n-1, L/3)
        # right(120)
        # courbe_von_koch(n-1, L/3)
        # left(60)
        # courbe_von_koch(n-1, L/3)

# Set up turtle
speed(0)
length = 300

# # Dessin
for _ in range(3):
     courbe_von_koch(4, length)
     right(120)
    #courbe_von_koch(3, length)
#done()
exitonclick()

