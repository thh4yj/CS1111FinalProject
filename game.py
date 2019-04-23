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
path1 = [gamebox.from_image(0,325,"14.png"),gamebox.from_image(75,325,"15.png"),gamebox.from_image(150,325,"15.png"),gamebox.from_image(225,325,"15.png"),gamebox.from_image(300,325,"15.png"),gamebox.from_image(375,325,"16.png"),gamebox.from_image(575,200,"14.png"),gamebox.from_image(650,200,"15.png"),gamebox.from_image(725,200,"15.png"),gamebox.from_image(800,200,"15.png"),gamebox.from_image(875,200,"16.png")]

for object in path1:
    object.scale_by(.6)
path2 = [gamebox.from_image(500,250,"14.png"),gamebox.from_image(575,250,"15.png"),gamebox.from_image(650,250,"15.png"),gamebox.from_image(725,200,""),gamebox.from_image(725,250,"15.png"),gamebox.from_image(800,250,"15.png"),gamebox.from_image(875,250,"15.png"),gamebox.from_image(950,250,"15.png"),gamebox.from_image(1025,250,"15.png"),gamebox.from_image(1100,250,"15.png"),gamebox.from_image(1175,250,"16.png")]
for object in path2:
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
        idle = gamebox.from_image(275,180,"Idle (1).png")
        idle.scale_by(.4)
        camera.draw(idle)
        if pygame.K_SPACE in keys:
            start_screen = False
            play = True

    elif play == True:


        # KEEP TRACK OF DISTANCE AND DISPLAY IT IN TOP RIGHT
        distance += 1/3
        camera.draw(gamebox.from_text(450,30,str(int(distance))+" m",25,"white"))


        # SLIDE WHEN DOWN ARROW PRESSED
        if pygame.K_DOWN in keys and jump == False:
            santa = gamebox.from_image(150, y_pos,slide_stages[frame])
            santa.scale_by(.2)
            camera.draw(santa)


        # JUMP WHEN UP ARROW PRESSED
        elif pygame.K_UP in keys:
            jump = True
            speed = 40
            santa = gamebox.from_image(150, y_pos, jump_stages[0])
            santa.scale_by(.2)
            camera.draw(santa)
            keys.clear()

        if jump:
            santa = gamebox.from_image(150, y_pos, jump_stages[jump_count])
            santa.scale_by(.2)
            camera.draw(santa)
            jump_count += 1
            if jump_count == 11:
                jump_count = 0
                jump = False


        # RUN
        if jump == False and not pygame.K_DOWN in keys:
            santa = gamebox.from_image(150, y_pos, run_stages[frame])
            santa.scale_by(.2)
            camera.draw(santa)


        # # STOPS CHARACTER STOPS WHEN IT HITS GROUND
        # if santa.y - speed >= 282:
        #     y_pos = 282
        #     camera.draw(santa)
        #     speed = 5


        # WILL ADD OBSTACLES AND/OR BLOCKS TO WALK ON
        for object in current_path:
            if object.x < -1000:
                current_path = paths[index + 1]
            camera.draw(object)
            if y_pos - speed > object.top -50 and santa.x < object.right and santa.x > object.left:
                y_pos = object.top - 50
                speed = 0
                jump = False
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
            camera.draw(gamebox.from_text(250, 75, "GAME OVER", 100, "white"))
            camera.draw(gamebox.from_text(250, 200, str(int(distance)) + " m", 200, "white"))


    camera.display()


gamebox.timer_loop(20, tick)