# Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.
import turtle as t

def draw_square(length):
    for _ in range(4):
        # print(t.heading())
        t.forward(length)
        t.left(90)

# Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita. Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempel:
# for x in range(5):
#     t.square()
#     t.move_next()
def move_pen_right_without_drawing(distance):
    # Lift pen
    t.penup()
    # Set heading to right (0).
    t.setheading(0)
    # Move distance.
    t.forward(distance)
    # Put pen back down.
    t.pendown()

# Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
# Tips 1: vad händer om man varierar värdet på range? 
# Tips 2: 360 grader motsvarar ett helt varv.
# for x in range(7):
#     t.forward(40)
#     t.right(30)
def draw_circle():
    for x in range(12): # Krävs 12 (360/30) segment för en hel cirkel.
        t.forward(40)
        t.right(30)
