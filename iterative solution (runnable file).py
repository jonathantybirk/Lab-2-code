# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit

import csv
with open("iterative solution data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Test#","Success?","Fuel"])
testNumber = 0

from LunarLander import *

env = LunarLander()
env.reset()
exit_program = False
while not exit_program:
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                env.reset()
                ticks = 0

    # INSERT YOUR CODE HERE
    #
    # Implement a Lunar Lander AI 
    # Control the rocket by writing a list of if-statements that control the 
    # three rockets on the lander 
    #
    # The information you have available are x, y, xspeed, and yspeed
    # 
    # You control the rockets by setting the variables boost, left, and right
    # to either True or false
    #
    # Example, to get you started. If the rocket is close to the ground, turn
    # on the main booster

    # if (yspeed-20)*(yspeed+20) / 1.5 >= 10*y:
    #     boost = True
    # else:
    #     boost = False

    if x < -5:
        right = False
        if xspeed < 10:
            left = True
        if xspeed > 15:
            left = False
    if x > 5:
        left = False
        if xspeed > -10:
            right = True
        if xspeed < -15:
            right = False

    if yspeed > 19:
        boost = True
    else:
        boost = False  
    # Modify and add more if-statements to make the rocket land safely
    # END OF YOUR CODE

    #log data
    if y<=0:
        testNumber += 1
        testData = [testNumber, env.won, env.rocket.fuel]
        with open("iterative solution data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(testData)
        print(f"test: {testData[0]}, success?: {testData[1]}, fuel left: {testData[2]}, finalSpeed: {yspeed}")
        env.reset()

env.close()