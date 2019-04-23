# Tyler Hendricks
# computingID: thh4yj


# Allison Branch and Tyler Hendricks
# computingIDs: aab4ad and thh4yj

# DESCRIPTION
# A winter themed side scrolling game in which a running character(santa), jumps and slides to avoid obstacles (trees, snowmen, etc.)
# and pass through multiple levels.

# REQUIRED FEATURES
# User Input --- Users will be able to control the character, pressing up to jump or down to slide and avoid obstacles
# Graphics/Images --- Game will have background images as well an animated character and obstacles
# Start Screen --- Game will have a start screen with title and basic game instructions

# OPTIONAL FEATURES
# Animation - The santa character will have animations for running, jumping and sliding
# Scrolling Level - The game will expand beyond the screen with new blocks and obstacles moving across the screen
# Multiple Levels - The game can have multiple levels with different obstacles
# Save Points - Allow users to return to checkpoints or to previous levels


# GAME CODE BELOW!!!

import pygame
import gamebox

# set up display
pygame.display.set_caption("SANTA RUN!")
screen_width = 500
screen_height = 400
camera = gamebox.Camera(screen_width,screen_height)


# IMAGES - all are from www.gameart2d.com
# -------- images and sprites are copyright/royalty free and free to use!

# walking animation images
run_stages = ["Run (1).png","Run (2).png","Run (3).png","Run (4).png","Run (5).png","Run (6).png",
                "Run (7).png","Run (8).png", "Run (9).png","Run (10).png","Run (11).png"]


# sliding animation images
slide_stages = ["Slide (1).png","Slide (2).png","Slide (3).png","Slide (4).png","Slide (5).png","Slide (6).png",
                "Slide (7).png","Slide (8).png","Slide (9).png","Slide (10).png","Slide (11).png"]

# jumping animation images
jump_stages = ["Jump (1).png","Jump (2).png","Jump (3).png","Jump (4).png","Jump (5).png","Jump (6).png",
               "Jump (7).png","Jump (8).png","Jump (9).png","Jump (10).png","Jump (11).png",
               "Jump (12).png","Jump (13).png", "Jump (14).png","Jump (15).png","Jump (16).png"]

# create background
background = gamebox.from_image(500/2,400/2,"BG.png")
background.scale_by(.45)

# create path
path1 = [gamebox.from_image(0,325,"14.png"),gamebox.from_image(75,325,"15.png"),gamebox.from_image(150,325,"15.png"),gamebox.from_image(225,325,"15.png"),gamebox.from_image(300,325,"15.png"),gamebox.from_image(375,325,"16.png"),gamebox.from_image(575,200,"14.png"),gamebox.from_image(650,200,"15.png"),gamebox.from_image(725,200,"15.png"),gamebox.from_image(800,200,"15.png"),gamebox.from_image(875,200,"16.png")
    ,gamebox.from_image(1150,400,"14.png"),gamebox.from_image(1225,400,"16.png"),gamebox.from_image(1425,350,"14.png"),gamebox.from_image(1500,350,"15.png"),gamebox.from_image(1575,350,"15.png"),gamebox.from_image(1575,350,"15.png"),gamebox.from_image(1650,350,"15.png"),gamebox.from_image(1725,350,"15.png"),gamebox.from_image(1800,350,"15.png"),gamebox.from_image(1875,350,"16.png")]



level_title1 = gamebox.from_text(300,50,"LEVEL 1",75,"white")
level_title2 = gamebox.from_text(300,-50,"LEVEL 2",75,"white")
level_title3 = gamebox.from_text(300,-50,"LEVEL 3",75,"white")




path2 = [gamebox.from_image(0,350,"14.png"),gamebox.from_image(75,350,"15.png"),gamebox.from_image(150,350,"15.png"),gamebox.from_image(225,350,"15.png"),
         gamebox.from_image(300,350,"15.png"),
         gamebox.from_image(375,350,"16.png"),gamebox.from_image(700,200,"Crate.png"),gamebox.from_image(500,250,"14.png"),gamebox.from_image(575,250,"15.png"),
         gamebox.from_image(650,250,"15.png"),gamebox.from_image(800,190,"SnowMan.png"),gamebox.from_image(725,250,"15.png"),
         gamebox.from_image(800,250,"16.png"),gamebox.from_image(950,350,"14.png"),gamebox.from_image(1000,350,"16.png"),
         gamebox.from_image(1200,250,"14.png"),gamebox.from_image(1250,250,"16.png"),gamebox.from_image(1450,150,"14.png"),gamebox.from_image(1500,150,"16.png"),gamebox.from_image(1700,350,"14.png"),gamebox.from_image(1775,350,"15.png"),
         gamebox.from_image(1850,350,"15.png"),gamebox.from_image(1925,350,"16.png")]

path3 = [gamebox.from_image(-75,150,"14.png"),gamebox.from_image(-25,150,"16.png"),gamebox.from_image(175,350,"14.png"),gamebox.from_image(250,350,"15.png"),
         gamebox.from_image(325,350,"15.png"),gamebox.from_image(400,350,"16.png")]




for object in path1:
    object.scale_by(.6)
for object in path3:
    object.scale_by
for object in path2:
    object.scale_by(.6)
for object in path3:
    object.scale_by(.6)

# initialize variables
start_screen = True
play = False
game_over = False
distance = 0
frame = 0
speed = 0
y_pos = 220
jump = False
jump_count = 0
paths = [path1,path2]
current_path = paths[0]
index = 0
level = 1
santa = gamebox.from_image(275, 180, "Idle (1).png")


# main loop
def tick(keys):

    global start_screen
    global play
    global game_over
    global distance
    global frame
    global speed
    global y_pos
    global jump
    global jump_count
    global current_path
    global index
    global paths
    global level
    global santa

    # DRAW BACKGROUND AND GROUND
    camera.draw(background)
    # for block in ground:
    #     camera.draw(block)

    # DISPLAY START SCREEN UNTIL PLAYER PRESSES SPACE
    # --- Should add game instructions later
    if start_screen:
        camera.draw(gamebox.from_text(250,40,"SANTA RUN",100,"white"))
        camera.draw(gamebox.from_text(250,310,"Press Space To Start",50,"white"))
        camera.draw(gamebox.from_text(240,200, "aab4ad                         thh4yj",40,"white"))
        santa = gamebox.from_image(275,180,"Idle (1).png")
        camera.draw(gamebox.from_text(250, 350, 'Hold the I key to view instructions', 30, 'white'))
        santa.scale_by(.4)
        if pygame.K_SPACE in keys:
            start_screen = False
            play = True
        if pygame.K_i in keys:
            camera.clear('white')
            camera.draw(background)
            instructions = ['The game will scroll at a constant speed.',
                            'It is the players job to navigate obstacles as ',
                            'they appear. Use the WASD or arrow',
                            'keys to navigate.',
                            'The players progress is saved at each ',
                            'level, allowing the player to restart the level',
                            'each time they die. The player will die if',
                            'they fall off the map or collide with an obstacle.']
            camera.draw(gamebox.from_text(250, 40, "INSTRUCTIONS", 80, "white"))
            y = 150
            for i in instructions:
                camera.draw(gamebox.from_text(250, y, i, 30, 'white'))
                y += 25

    elif play == True:


        # KEEP TRACK OF DISTANCE AND DISPLAY IT IN TOP RIGHT
        distance += 1/3
        camera.draw(gamebox.from_text(450,30,str(int(distance))+" m",25,"white"))


        # SLIDE WHEN DOWN ARROW PRESSED
        if pygame.K_DOWN in keys and jump == False:
            santa = gamebox.from_image(150, y_pos,slide_stages[frame])
            santa.scale_by(.2)


        # JUMP WHEN UP ARROW PRESSED
        elif (pygame.K_UP in keys or pygame.K_w in keys) and y_pos >= 20:
            jump = True
            speed = 40
            santa = gamebox.from_image(150, y_pos, jump_stages[0])
            santa.scale_by(.2)
            keys.clear()

        if jump:
            santa = gamebox.from_image(150, y_pos, jump_stages[jump_count])
            santa.scale_by(.2)
            jump_count += 1
            if jump_count == 11:
                jump_count = 0
                jump = False


        # RUN
        if jump == False and not pygame.K_DOWN in keys:
            santa = gamebox.from_image(150, y_pos, run_stages[frame])
            santa.scale_by(.2)


        # OBSTACLES OR BLOCKS TO WALK ON

        camera.draw(level_title1)
        level_title1.move(0,-5)
        camera.draw(level_title2)
        level_title2.move(0,-5)
        camera.draw(level_title3)
        level_title3.move(0,-5)


        for object in current_path:
            camera.draw(object)
            if y_pos - speed > object.top -50 and santa.x < object.right and santa.x > object.left:
                y_pos = object.top - 50
                speed = 0
                jump = False

            if object.x < -1500 and level == 2:
                current_path = path3
                print("LEVEL 3")
                distance = 0
                level_title3.y = 50

            if object.x < -1500 and level == 1:
                print("LEVEL 2")
                current_path = path2
                distance = 0
                level += 1
                level_title2.y = 50



            object.move(-10,0)



        # CHARACTER'S Y POSITION CHANGES BY THEIR SPEED AND DOWNWARD SPEED INCREASES (GRAVITY)
        y_pos = y_pos - speed
        speed -= 5

        # KEEPS TRACK OF THE ANIMATION FRAMES FOR RUNNING AND SLIDING
        frame += 1
        if frame == 11:
            frame = 0


        # CHECK FOR GAME OVER
        if y_pos > 400:
            play = False
            game_over = True


    # DISPLAY END SCREEN WHEN GAME IS OVER
    # --- add way to restart game (possibly at a checkpoint)
    elif game_over:
        camera.draw(gamebox.from_text(250, 50, "GAME OVER", 100, "white"))
        camera.draw(gamebox.from_text(250, 200, str(int(distance)) + " m", 200, "white"))
        camera.draw(gamebox.from_text(250,350,"Press R to restart level",50,"white"))
        if pygame.K_r in keys:
            if current_path == path1:
                for object in path1:
                    object.move(distance*3*10,0)
                level_title1.y = 50
            if current_path == path2:
                for object in path2:
                    object.move(distance*3*10,0)
                level_title2.y = 50
            if current_path == path3:
                for object in path3:
                    object.move(distance*3*10,0)
                level_title2.y = 50


            y_pos = 230
            speed = 0
            distance = 0
            game_over = False
            play = True



    camera.draw(santa)
    camera.display()


gamebox.timer_loop(20, tick)