import turtle as t
from turtle_graphics.draw import draw_square, move_pen_right_without_drawing, draw_circle
import turtle_graphics.draw_letters as letters

# Lista alternativen.
text_alternativ = [
    "Rita kvadrat",
    "Rita flera kvadrater",
    "Rita cirkel",
    "Rita PYTHON"
]
# Lägg till siffra för varje alternativ.
for i in range(len(text_alternativ)):
    text_alternativ[i] = f'{i}. {text_alternativ[i]}'

# Be användaren välja ett alternativ.
while True:
    valt_alternativ = int(input(f"Välj ett alternativ:\n\t{'\n\t'.join(text_alternativ)}\n"))
    if valt_alternativ in range(len(text_alternativ)):
        break
    else:
        print("Felaktigt alternativ, försök igen.")

if valt_alternativ == 0:
    # Rita en kvadrat.
    draw_square(100)
elif valt_alternativ == 1:
    # Rita en kvadrat.
    draw_square(100)
    # Flytta åt höger utan att rita.
    move_pen_right_without_drawing(150)
    # Rita en till kvadrat.
    draw_square(50)
elif valt_alternativ == 2:
    # Rita en cirkel
    draw_circle()

elif valt_alternativ == 3:
    t.speed(0)
    letters.draw_python()

t.mainloop()