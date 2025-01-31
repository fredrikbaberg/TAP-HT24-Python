# Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen. Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.

import turtle as t
from math import cos, sin, sqrt
from turtle_graphics.draw import move_pen_right_without_drawing
letter_height = 100
letter_width = 50
letter_spacing = 10

# Kommer rita upp varje bokstav nedifrån och upp.

# Rita upp bokstaven P
def draw_p():
    t.left(90) # "Tittar" uppåt.
    t.forward(100) # Flytta uppåt 100 pixlar.
    t.right(90) # "Tittar" tillbaka åt höger.
    # Rita halvcirkeln för P. Använder circle() i stället.
    t.circle(-25, 180)

# Rita bokstaven Y.
def draw_y():
    # Utgå från mitten av basen.
    t.penup()
    t.forward(letter_width/2)
    t.pendown()
    t.left(90) # Tittar uppåt.
    t.forward(letter_height/2) # Halvvägs upp.
    for i in [1,-1]: # Rita bägge "armar"
        t.left(i*30)
        # Ska egentligen skala längden för att nå hela vägen upp.
        skalfaktor = 1.11 # Gissning.
        t.forward(skalfaktor*(letter_height/2))
        t.backward(skalfaktor*(letter_height/2))
        t.right(i*30)

def draw_t():
    # Flytta en bit åt höger.
    t.penup()
    t.forward(20)
    t.pendown()
    t.left(90)
    t.forward(letter_height)
    t.left(90)
    t.forward(20)
    t.backward(2*20)

def draw_h():
    t.left(90)
    t.forward(letter_height)
    t.backward(letter_height/2)
    t.right(90)
    t.forward(letter_width)
    t.left(90)
    t.forward(letter_height/2)
    t.backward(letter_height)

def draw_o():
    t.penup()
    t.forward(letter_width/2)
    t.pendown()
    for x in range(12):
        t.forward(letter_width/(12/2))
        t.left(30)

def draw_n():
    t.left(90)
    t.forward(letter_height)
    t.right(90 + 60)
    t.forward(sqrt(letter_height**2+letter_width**2))
    t.left(90+60)
    t.forward(letter_height)

# Flytta pennan till ny position.
# I stället för 'död räkning' används inbyggda funktioner.
def move_pen(letter_number):
    t.penup()
    t.setpos([letter_number*(letter_width+letter_spacing), 0])
    t.setheading(0) # Titta åt höger.
    t.pendown()

# Rita linje i en annan färg. Återställ färgen efteråt.
def draw_base_lines(length):
    color_previous = t.color()
    t.color("red")
    t.forward(length)
    t.penup()
    t.setposition(0,letter_height)
    t.pendown()
    t.forward(length)
    t.color(color_previous[0], color_previous[1])

# Rita upp ordet PYTHON.
def draw_python():
    letters = [draw_p, draw_y, draw_t, draw_h, draw_o, draw_n]
    # Börja med att rita en linje, för att se om det blir rakt.
    draw_base_lines(letter_width*(len(letters)+1))

    for i in range(len(letters)):
        move_pen(i)
        print(f"Skriv ut {i}, startar på {t.position()}")
        letters[i]()

if __name__=='__main__':
    draw_python()
    t.mainloop()
