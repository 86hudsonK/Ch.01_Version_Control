'''
1.0 Jedi Training (17pts)  Name:Hudson Kerchal


1. Define Forking (1pt):
 making a copy of a repository
from an organization to my account on GitHub

2. Define Cloning (1pt): 

3. Define Branching (1pt):

4. Define Committing (1pt): 

5. Define Merging (1pt): 

6. Define Pushing (1pt):

7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('lavender')
t.color('white')
a=0
b=0
t.speed(0)
t.penup()
t.goto(-10,180)
t.pendown()
while True:
  t.forward(a)
  t.right(b)
  a+=3
  b+=1
  if b ==210:
    break
  t.hideturtle()
t.penup()
t.goto(-195,180)
t.write('Hudson Kerchal')
turtle.done()




turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
