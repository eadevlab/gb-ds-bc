import turtle
import time


def main(iterations, axiom, rules, angle, length=8, size=2, y_offset=0, x_offset=0, offset_angle=0, width=450, heigth=450):
    def draw_l_system(t, instructions, angle, distance):
        for cmd in instructions:
            if cmd == 'F':
                t.forward(distance)
            elif cmd == '+':
                t.right(angle)
            elif cmd == '-':
                t.left(angle)

    def create_instruction(start_string, rules):
        return "".join(rules[i] if i in rules else i for i in start_string)

    def reset(t):
        t.reset()
        t.backward(-x_offset)
        t.left(90)
        t.backward(-y_offset)
        t.left(offset_angle)
        t.down()
        t.speed(0)
        t.pensize(size)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, heigth)

    t.up()
    for i in range(iterations):
        turtle.title("Итерация №%s" % (i+1))
        reset(t)
        if i > 0:
            axiom = create_instruction(axiom, rules)
        draw_l_system(t, axiom, angle, length)
        time.sleep(3)
    t.hideturtle()
    wn.exitonclick()


# axiom = "F+F+F+F"
# rules = {"F": "F-F+F+FFF-F-F+F"}
# iterations = 3  # top:4
# angle = 90

# Треугольник
# axiom = "F+F+F"
# rules = {"F":"F-F+F"}
# iterations = 6 # TOP: 9
# angle = 120

# Кривая дракона
# axiom = "FX"
# rules = {"X":"X+YF+", "Y":"-FX-Y"}
# iterations = 8 # TOP: 16
# angle = 90

# Кольца
# axiom = "F+F+F+F"
# rules = {"F":"FF+F+F+F+F+F-F"}
# iterations = 4 # TOP: 4
# angle = 90

# Решетка Серпинского
axiom = "FXF--FF--FF"
rules = {"F":"FF", "X":"--FXF++FXF++FXF--"}
iterations = 7 # TOP: 8
angle = 60

if __name__ == '__main__':
    main(iterations, axiom, rules, angle)
