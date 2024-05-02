import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():

    try:
        level = int(input("Введіть рівень рекурсії (ціле число >= 0): "))
    except ValueError:
        print("Неправильний формат вводу. Рівень рекурсії має бути цілим числом.")
        return
    
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=800, height=600) 
    window.tracer(0) 

    snowflake = turtle.Turtle()
    snowflake.color("blue")
    snowflake.speed(0)  
    
    snowflake.penup()
    snowflake.goto(-150, 100) 
    snowflake.pendown()

    for _ in range(3):
        koch_snowflake(snowflake, level, 300)
        snowflake.right(120)
    
    window.update()
    input("Натисніть Enter для виходу...")
    window.bye()

if __name__ == "__main__":
    main()
