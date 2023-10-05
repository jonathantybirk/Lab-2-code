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
with open("optimized solution data.csv", "w", newline="") as file:
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
    timeleft = 0
   # print(y,yspeed,y/yspeed/20,np.sqrt(2*y/1.5),((yspeed)**2)/3 > y*10)
    #if not boost:

    if ((yspeed)**2)/3 > y*10:
        boost = True
        yt = y
        yst = yspeed
        time = 0
        while yt > 0:
            yt -= yst * 0.1
            yst -= 1.5
            time += 1
        timeleft = time
    else:
        boost = False
        yt = y
        yst = yspeed
        time = 0
        while ((yst)**2)/3 < yt*10:
            time += 1
            yt -= yst * 0.1
            yst += 1
        while yt > 0:
            yt -= yst * 0.1
            yst -= 1.5
            time += 1
        timeleft = time
    
    ex = x+xspeed*timeleft/10
    if xspeed > 20: #if too fast the left
        if ((xspeed + 20)/2) * timeleft > -20 and (xspeed - 20)/2 > timeleft - 1:
            right = True
            left = False
        elif ex < 0:#on the left
            left = True
            right = False
        else:
            right = left = False
    elif xspeed < -20: #if too fast the right
        if abs((xspeed + 20)/2) > timeleft - 1:#((xspeed - 20)/2) * timeleft > 20 and 
            right = False
            left = True
        elif ex > 0:#on the right
            right = True
            left = False
        else:
            right = left = False
    elif ex > 20:#on the right
        right = True
        left = False
           # print('start')
    elif ex < -20:#on the left
        left = True
        right = False

    else:
        left = right = False


      #  print('f')
#    print(x,xspeed)

    # if abs(x) > 10 or abs(xspeed) > 10: # 2 speed per tick, .1 speed x per speed per tick
    #     xtik = abs(xspeed)/2
    #     #if timleft*xspeed - x < 0:
    #     if abs(xtik * xspeed /2 + x) < 15:
    #         if x > 10:
    #             left = True
    #             right = False
    #         elif x< 10:
    #             right = True
    #             left = False
    #     elif abs(xtik * xspeed /2 + x) > 50:
    #         if x > 10:
    #             right = True
    #             left = False
    #         elif x< 10:
    #             left = True
    #             right = False
           # print(abs(xtik * xspeed /2 + x),x,xspeed)
    # if yspeed > 10:
    #     boost = True
    # if yspeed < 5:
    #     boost = False
    # if y > 200:
    #     boost = False
    # if y < 10 and abs(x)>20:
    #     boost = True
    # if x > 10 or xspeed > 10:
    #     right = True
    # if x < -10 or xspeed < -10:
    #     left = True
    # if left and right:
    #     left = right = False     
    # if abs(x)<15 and abs(xspeed)<=1:
    #     left = right = False

    #log data
    if y<=0:
        testNumber += 1
        testData = [testNumber, env.won, env.rocket.fuel]
        with open("optimized solution data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(testData)
        print(f"test: {testData[0]}, success?: {testData[1]}, fuel left: {testData[2]}, finalSpeed: {yspeed}")
        env.reset()


    # Modify and add more if-statements to make the rocket land safely
    # END OF YOUR CODE

env.close()