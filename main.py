# imports
import turtle
import random
import math

# Game Screen
s = turtle.Screen()
s.setup(320,320)
s.screensize(300,300)
s.bgpic("BG.gif")

s.addshape('Spider.gif')
img = ("Spider.gif")
spider = turtle.Turtle()
s.addshape(img)
spider.shape(img)
spider.penup()
spider.showturtle()
spider.setpos(0,-100)
spider.width()
s.tracer(0)

t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()
t.penup()  
w, h = s.screensize()
img = ("spiderweb.gif")
goal = turtle.Turtle()
Goal = turtle.Turtle()
s.addshape(img)
goal.shape(img)
Goal.shape(img)
goal.penup()
Goal.penup()
goal.setpos(70,130)
Goal.setpos(-70,130)


# <variable declaractions>
lives = 3
level = 1
score = 0
gamestate = "Play" 

# <function definitions>
def start_screen():
  s = turtle.Screen()
  s.setup(320,320)
  s.screensize(300,300)
  s.bgpic("BG.gif")
  s.addshape('Spider.gif')
  t = turtle.Turtle()
  w, h = s.screensize()
  img = ("Spider.gif")
  return startscreen

harms = []

def harm( y_pos, image, obj_type):
  harms.append({"t": turtle.Turtle() ,"x":random.randint(-100,100), "y":y_pos, "width": 30,"radius": 30,"image":image, "type":obj_type, "speed": .1,"pen":turtle.penup()})
  return harms

def isCollision():
  for harm in harms:
    if (harm["t"].distance(spider) < (harm["radius"])):
      spider.setpos(0, -100)
      print(harm["t"].distance(spider))
      return True


def update_values ():
  t.clear()
  t.setpos(-145, 140)
  t.write("Lives: " + str(lives), font=("Arial", 12, "bold"))
  t.setpos(-145,125)
  t.write("Level: " + str(level), font = ("Arial", 12, "bold"))
  t.setpos(-145,110)
  t.write("Score: " + str(score), font = ("Arial", 12, "bold"))  
  return update_values

def game_Over():
  s.clear()
  s.bgpic("GameOver.gif")
  update_values()
  return game_Over

harm(80,"Bird.gif","harm")
harm(20,"Bird(left).gif","harm")
harm(-20,"Bird.gif","harm")
harm(-70,"Bird(left).gif","harm")

update_values()

def main():
  # <keypress event handler> #declared inside main due to scope issues
  def up():
    spider.setheading(90)
    spider.forward(50)

  def down():
    spider.setheading(270)
    spider.forward(50)

  def right():
    spider.setheading(360)
    spider.forward(50)

  def left():
    spider.setheading(180)
    spider.forward(50)

  def start():
    print ("start")

  s.onkey(up,'Up')
  s.onkey(down, 'Down')
  s.onkey(right,'Right')
  s.onkey(left,'Left')
  s.onkey(start, "space")


  # Update values
  for harm in harms:
    s.addshape(harm["image"])
    harm["t"].shape(harm["image"])
    img = harm["image"]
    t = harm["t"]
    s.addshape(img)
    t.shape(img)
    
  while (lives > 0):

    #<function definitions>
    def get_level():
      global level
      level = level + 1
      return level

    def get_lives():
      global lives
      lives = lives - 1
      return lives

    def get_score():
      global score
      score = score + 100
      return score

    def level_up():
      get_score()
      get_level()
      for harm in harms:
        harm["speed"] = harm["speed"] + .1
      spider.setpos(0,-100)

    for harm in harms:
      harm["t"].clear()
      t = harm["t"]
      x = harm["x"]
      y = harm["y"]
      t.goto(x,y)

    # <animation loop>
      if (harm["type"] == "harm") and (harm["image"] == "Bird.gif"):
        harm["t"].clear()
        harm["x"] += harm["speed"]
        if (harm["type"] == "harm") and (harm["x"] >= (w+harm["radius"])/2):
          harm["x"] = -w/2 - 50

      if (harm["type"] == "harm") and (harm["image"] == "Bird(left).gif"):
        harm["t"].clear()
        harm["x"] -= harm["speed"] 
        if (harm["type"] == "harm") and (harm["x"] <= -(w/2)-harm["radius"]):
          harm["x"] = w/2 + 50

    # <spider edge of screen>
      if (spider.xcor() <= -(w/2) - 30):
        spider.setpos(125,-100)
      if (spider.xcor() >= (w/2) + 20):
        spider.setpos(-130,-100)

      if isCollision():
        print (get_lives())
        update_values()

      if (spider.ycor() > 130):
        level_up()
        print (harm["speed"])
        update_values()



    s.listen()
    s.update()

  #<game over screen>    
  game_Over()  
  return main

main()