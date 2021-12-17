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
t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()  
w, h = s.screensize()
img = ("Spider.gif")
t.penup()
t.goto(70, 125)
t.write("Lives: 3", font=("Arial", 14, "bold"))
t.penup()
t.goto(-145,125)
t.write("Score: 0", font = ("Arial", 14, "bold"))


spider = turtle.Turtle()
s.addshape(img)
spider.shape(img)
spider.penup()
spider.showturtle()
spider.setpos(0,-100)
spider.width()
s.tracer(0)

# <variable declaractions>
lives = 3
level = 1
score = 0
gamestate = "Play" 


# <function definitions>
def startscreen():
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
  harms.append({"t": turtle.Turtle() ,"x":random.randint(-100,100), "y":y_pos, "width": 30,"radius": 30,"image":image, "type":obj_type, "speed":1,"pen":turtle.penup()})
  return harms

def isCollision():
  for harm in harms:
    if (harm["t"].distance(spider) < (harm["radius"])):
      spider.setpos(0, -100)
      print(harm["t"].distance(spider))
      return True

harm(70,"Bird.gif","harm")
harm(20,"Bird(left).gif","harm")
harm(-20,"Bird.gif","harm")
harm(-70,"Bird(left).gif","harm")

def updatevalues ():
  t.clear()
  t.hideturtle
  t.penup()
  t.goto(70, 125)
  t.write("Lives:" + str(lives), font=("Arial", 14, "bold"))
  t.penup()
  t.goto(-145,125)
  t.write("Score:" + str(score), font = ("Arial", 14, "bold"))
  return updatevalues

def gameOver():
  return gameOver



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

  print (harms[0]["t"].distance(spider))
  print (harms[1]["t"].distance(spider))
  print (harms[2]["t"].distance(spider)) 
  print (harms[3]["t"].distance(spider)) 

  for harm in harms:
    print (harm["t"].distance(spider))
  #   #  <start screen>

  # Update values
  for harm in harms:
    s.addshape(harm["image"])
    harm["t"].shape(harm["image"])

    img = harm["image"]
    t = harm["t"]
    s.addshape(img)
    t.shape(img)
    
  while (lives > 0):
    for harm in harms:
      harm["t"].clear()

    for harm in harms:
      t = harm["t"]
      x = harm["x"]
      y = harm["y"]
      t.goto(x,y)

    # <animation loop>
      if (harm["type"] == "harm") and (harm["image"] == "Bird.gif"):
        harm["t"].clear()
        harm["x"] += .1
        if (harm["type"] == "harm") and (harm["x"] >= (w+harm["radius"])/2):
          harm["x"] = -w/2 - 50

      if (harm["type"] == "harm") and (harm["image"] == "Bird(left).gif"):
        harm["t"].clear()
        harm["x"] -= .1
        if (harm["type"] == "harm") and (harm["x"] <= -(w/2)-harm["radius"]):
          harm["x"] = w/2 + 50

      def get_lives():
       global lives
       lives = lives - 1
       return lives

      if isCollision():
        print (get_lives())
        updatevalues()


     

     #   #  <game over screen>
    


    s.listen()
    s.update()
    
  return main







main()