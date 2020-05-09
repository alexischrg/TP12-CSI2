import turtle

def drawCurve(turtle,l,n):
    if n == 0:
        turtle.forward(l)
        return
    else:
        l /= 3
        drawCurve(turtle,l,n-1)
        turtle.left(60)
        drawCurve(turtle,l,n-1)
        turtle.right(120)
        drawCurve(turtle,l,n-1)
        turtle.left(60)
        drawCurve(turtle,l,n-1)

def drawFullCurve(turtle,l,n):
    for i in range(3):
        drawCurve(turtle,l,n)
        turtle.right(120)


if __name__ == "__main__" :
    turtle.setup(800,400)
    #drawCurve(turtle,300,2)
    #turtle.exitonclick()

    turtle.tracer(False)
    turtle.hideturtle()
    turtle.color("cyan")
    drawFullCurve(turtle,200,3)
    turtle.tracer(True)
    turtle.exitonclick()