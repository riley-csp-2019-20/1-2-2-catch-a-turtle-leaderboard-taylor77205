# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random 
import leaderboard as lb 

#-----game configuration----
shape = "turtle"
size = 5
color = "purple"
score = 0

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----leaderboard variables----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("please enter your name")

#-----initialize turtle-----
T = trtl.Turtle(shape=shape)
T.color(color)
T.shapesize(size)

scoreboard= trtl.Turtle()
scoreboard.penup()
scoreboard.goto(-270,270)
font = ("Arial", 60,"bold") 
scoreboard.write(score,font=font)
scoreboard.ht()
counter =  trtl.Turtle()
counter.goto (270,-270)

#-----game functions--------
def turtle_clicked(x,y):
    print("T was clicked")
    change_position()
    score_counter()

def change_position():
    T.penup()
    T.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-400,400)
    T.goto(new_xpos,new_ypos)
    T.st()

def score_counter():
    global score
    score += 1
    print (score)
    scoreboard.clear()
    scoreboard.write(score,font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.goto(0,0)
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def game_over():
    T.ht()
    T.goto(520,500)

def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global T

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, T, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, T, score)


#-----events----------------
T.onclick(turtle_clicked)


wn=trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()