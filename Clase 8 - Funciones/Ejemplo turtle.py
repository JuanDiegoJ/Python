import turtle

def main():
    window = turtle.Screen()
    juan = turtle.Turtle()
    make_square(juan)
    turtle.mainloop()

def make_square(juan):
    length = int(input('Tamaño del cuadrado: '))
    for i in range (4):
        make_line_and_turn(juan, length)

def make_line_and_turn(juan, length):
    juan.forward(length)
    juan.left(90)
    
if __name__ == '__main__':
   main()