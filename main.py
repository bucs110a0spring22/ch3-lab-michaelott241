import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
randomichel = random.randrange(1,10)
michelangelo.forward(randomichel)
randoleonardo = random.randrange(1,10)
leonardo.forward(randoleonardo)
print(randomichel)
print(randoleonardo)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


for i in range(10):
  distance = random.randrange(0,10)
  length = random.randrange(0,10) 
  michelangelo.forward(distance)
  leonardo.forward(length)
  print(distance)
  print(length)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# Part B - complete part B here
sides = [3,4,6,9,12]
for side in sides:
  angle=360/side
  length = 20
  for i in range(side):
    michelangelo.down()
    michelangelo.right(angle)
    michelangelo.forward(length)
    michelangelo.up()
  michelangelo.clear()


window.exitonclick()
