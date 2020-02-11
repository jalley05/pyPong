# Turle graphics
import turtle
import time

# Game Object
class Game:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("PyPong")
        self.wn.bgcolor("black")
        self.wn.setup(width=1000, height=800)
        self.wn.tracer(0) # Prevent auto draw

        # init paddle A and listener
        self.__paddleA = self.Paddle(-475)
        self.wn.onkeypress(self.__paddleA.moveUp, 'w')
        self.wn.onkeypress(self.__paddleA.moveDown, 's')
        
        self.__paddleB = self.Paddle(475)
        self.wn.onkeypress(self.__paddleB.moveUp, 'Up')
        self.wn.onkeypress(self.__paddleB.moveDown, 'Down')

        # init the ball
        self.__ball = self.Ball()
       
        self.wn.listen()

    def updateWindow(self):
        self.wn.update()
        self.__ball.update()
 
    ## Paddle Sub Object ##
    class Paddle:
        def __init__(self, beginCoord):
            self.turtleObj = turtle.Turtle()
            self.turtleObj.speed(0)
            self.turtleObj.shape("square")
            self.turtleObj.color('white')
            self.turtleObj.penup()
            self.turtleObj.goto(beginCoord, 0)
            self.turtleObj.shapesize(stretch_wid=5, stretch_len=1)

        def incrX(self, xIncr):
            self.turtleObj.setx(self.turtleObj.xcor() + xIncr)


        def moveUp(self):
            curY = self.turtleObj.ycor()
            curY += 20
            self.turtleObj.sety(min(curY, 400-50))

        def moveDown(self):
            curY = self.turtleObj.ycor()
            curY -= 20
            self.turtleObj.sety(max(curY, -400+50))


    class Ball:
        def __init__(self):
            self.turtleObj = turtle.Turtle()
            self.turtleObj.speed(0)
            self.turtleObj.shape("square")
            self.turtleObj.color("white")
            self.turtleObj.penup()
            self.turtleObj.goto(0, 0)

        def update(self):
            curX = self.turtleObj.xcor()
            curX += 20
            self.turtleObj.setx(max(curX, 350))

            curY = self.turtleObj.ycor()
            curY += 20
            self.turtleObj.sety(max(curY, 350))

            time.sleep(0.5)



gameWindow = Game()



# Main game loop
while True:
    gameWindow.updateWindow()
