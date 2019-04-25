# Allison Branch and Tyler Hendricks
# computingIDs: aab4ad and thh4yj

# DESCRIPTION
# A winter themed side scrolling game in which a running character(santa), jumps and slides to avoid obstacles (
# trees, snowmen, etc.)
# and pass through multiple levels.

# REQUIRED FEATURES
# User Input --- Users will be able to control the character, pressing up to jump or down to slide and avoid obstacles
# Graphics/Images --- Game will have background images as well an animated character and obstacles
# Start Screen --- Game will have a start screen with title and basic game instructions

# OPTIONAL FEATURES
# Animation - The santa character will have animations for running, jumping and sliding
# Scrolling Level - The game will expand beyond the screen with new blocks and obstacles moving across the screen
# Multiple Levels - The game can have multiple levels with different obstacles
# Save Points - Allow users to return to beginning of level or to previous levels


# GAME CODE BELOW!!!

import pygame
import gamebox

# set up display
pygame.display.set_caption("SANTA RUN!")
screen_width = 500
screen_height = 400
camera = gamebox.Camera(screen_width, screen_height)


# IMAGES - all are from www.gameart2d.com
# -------- images and sprites are copyright/royalty free and free to use!

# walking animation images
run_stages = ["Run (1).png", "Run (2).png", "Run (3).png", "Run (4).png", "Run (5).png", "Run (6).png",
              "Run (7).png", "Run (8).png", "Run (9).png", "Run (10).png", "Run (11).png"]


# sliding animation images
slide_stages = ["Slide (1).png", "Slide (2).png", "Slide (3).png", "Slide (4).png", "Slide (5).png", "Slide (6).png",
                "Slide (7).png", "Slide (8).png", "Slide (9).png", "Slide (10).png", "Slide (11).png"]

# jumping animation images
jump_stages = ["Jump (1).png", "Jump (2).png", "Jump (3).png", "Jump (4).png", "Jump (5).png", "Jump (6).png",
               "Jump (7).png", "Jump (8).png", "Jump (9).png", "Jump (10).png", "Jump (11).png",
               "Jump (12).png", "Jump (13).png", "Jump (14).png", "Jump (15).png", "Jump (16).png"]

# create background
background = gamebox.from_image(500/2, 400/2, "BG.png")
background.scale_by(.45)

# make tree
tree = gamebox.from_image(800, 175, "Tree_1.png")
tree.scale_by(.8)


# create levels
level1 = [gamebox.from_image(0, 325, "14.png"), gamebox.from_image(75, 325, "15.png"),
          gamebox.from_image(150, 325, "15.png"), gamebox.from_image(225, 325, "15.png"),
          gamebox.from_image(300, 325, "15.png"), gamebox.from_image(375, 325, "16.png"),
          gamebox.from_image(575, 250, "14.png"), gamebox.from_image(650, 250, "15.png"),
          gamebox.from_image(725, 250, "15.png"), gamebox.from_image(800, 250, "15.png"),
          gamebox.from_image(875, 250, "16.png"), gamebox.from_image(1000, 150, "14.png"),
          gamebox.from_image(1075, 150, "15.png"), gamebox.from_image(1150, 150, "15.png"),
          gamebox.from_image(1225, 150, "16.png"), gamebox.from_image(1425, 350, "14.png"),
          gamebox.from_image(1500, 350, "15.png"), gamebox.from_image(1575, 350, "15.png"),
          gamebox.from_image(1575, 350, "15.png"), gamebox.from_image(1650, 350, "15.png"),
          gamebox.from_image(1725, 350, "15.png"), gamebox.from_image(1800, 350, "15.png"),
          gamebox.from_image(1875, 350, "16.png"), gamebox.from_image(1875, 290, "Crate.png"),
          gamebox.from_image(1550, 290, "Crate.png")]

level2 = [gamebox.from_image(25, 350, "15.png"), gamebox.from_image(100, 350, "15.png"),
          gamebox.from_image(125, 350, "15.png"), gamebox.from_image(200, 350, "15.png"),
          gamebox.from_image(275, 350, "15.png"), gamebox.from_image(350, 350, "16.png"),
          gamebox.from_image(350, 290, "Crate.png"), gamebox.from_image(700, 200, "Crate.png"),
          gamebox.from_image(500, 250, "14.png"), gamebox.from_image(575, 250, "15.png"),
          gamebox.from_image(650, 250, "15.png"), gamebox.from_image(800, 190, "SnowMan.png"),
          gamebox.from_image(725, 250, "15.png"), gamebox.from_image(800, 250, "16.png"),
          gamebox.from_image(950, 350, "14.png"), gamebox.from_image(1000, 350, "16.png"),
          gamebox.from_image(1200, 250, "14.png"), gamebox.from_image(1250, 250, "16.png"),
          gamebox.from_image(1450, 150, "14.png"), gamebox.from_image(1500, 150, "16.png"),
          gamebox.from_image(1700, 350, "14.png"), gamebox.from_image(1775, 350, "15.png"),
          gamebox.from_image(1850, 350, "15.png"), gamebox.from_image(1925, 350, "16.png")]

level3 = [gamebox.from_image(-75, 150, "14.png"), gamebox.from_image(-25, 150, "16.png"),
          gamebox.from_image(175, 350, "14.png"), gamebox.from_image(250, 350, "15.png"),
          gamebox.from_image(325, 350, "15.png"), gamebox.from_image(400, 350, "16.png"),
          gamebox.from_image(500, 250, "14.png"), gamebox.from_image(575, 250, "15.png"),
          gamebox.from_image(650, 250, "15.png"), gamebox.from_image(725, 250, "15.png"),
          gamebox.from_image(800, 250, "15.png"), gamebox.from_image(875, 250, "15.png"),
          gamebox.from_image(950, 250, "16.png"), gamebox.from_image(700, 200, "Crate.png"),
          gamebox.from_image(700, 150, "Crate.png"), tree,
          gamebox.from_image(1140, 350, "14.png"), gamebox.from_image(1160, 350, "16.png"),
          gamebox.from_image(1340, 250, "14.png"), gamebox.from_image(1360, 250, "16.png"),
          gamebox.from_image(1540, 125, "14.png"), gamebox.from_image(1600, 125, "16.png"),
          gamebox.from_image(1610, 350, "14.png"), gamebox.from_image(1685, 350, "15.png"),
          gamebox.from_image(1760, 350, "15.png"), gamebox.from_image(1835, 350, "15.png"),
          gamebox.from_image(1900, 350, "16.png")
          ]

level4 = [gamebox.from_image(-75, 125, "14.png"), gamebox.from_image(-50, 125, "16.png"),
          gamebox.from_image(90, 125, "14.png"), gamebox.from_image(150, 125, "16.png"),
          gamebox.from_image(170, 350, "14.png"), gamebox.from_image(245, 350, "15.png"),
          gamebox.from_image(320, 350, "15.png"), gamebox.from_image(395, 350, "15.png"),
          gamebox.from_image(470, 350, "16.png"), gamebox.from_image(560, 250, "14.png"),
          gamebox.from_image(625, 250, "16.png"), gamebox.from_image(825, 250, "14.png"),
          gamebox.from_image(890, 250, "16.png"), gamebox.from_image(850, 175, "Snowman.png"),
          gamebox.from_image(590, 200, "Stone.png"), gamebox.from_image(1191, 310, 'Crystal.png'),
          gamebox.from_image(1175, 350, "14.png"), gamebox.from_image(1240, 350, "16.png"),
          gamebox.from_image(1450, 250, "14.png"), gamebox.from_image(1500, 250, "16.png"),
          gamebox.from_image(1540, 125, "14.png"), gamebox.from_image(1560, 125, "16.png")]


for object in level1:
    object.scale_by(.6)
for object in level2:
    object.scale_by(.6)
for object in level3:
    object.scale_by(.6)
for object in level4:
    object.scale_by(.6)

level_title1 = gamebox.from_text(255, 75, "LEVEL 1", 100, "white")
level_title2 = gamebox.from_text(255, -100, "LEVEL 2", 100, "white")
level_title3 = gamebox.from_text(255, -100, "LEVEL 3", 100, "white")
level_title4 = gamebox.from_text(255, -100, 'LEVEL 4', 100, 'white')


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
current_level = level3
level = 3
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
    global current_level
    global level
    global santa

    # DRAW BACKGROUND
    camera.draw(background)

    # DISPLAY START SCREEN UNTIL PLAYER PRESSES SPACE OR I TO VIEW INSTRUCTIONS
    if start_screen:
        camera.draw(gamebox.from_text(250, 40, "SANTA RUN", 100, "white"))
        camera.draw(gamebox.from_text(250, 310, "Press Space To Start", 50, "white"))
        camera.draw(gamebox.from_text(240, 200, "aab4ad                         thh4yj", 40, "white"))
        santa = gamebox.from_image(275, 180, "Idle (1).png")
        camera.draw(gamebox.from_text(250, 350, 'Hold the I key to view instructions', 30, 'white'))
        santa.scale_by(.4)
        camera.draw(santa)

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

    elif play is True:

        # DISPLAY PERCENT OF LEVEL COMPLETED IN TOP RIGHT --> each level has a distance of 50
        distance += 1/3
        if distance > 50:
            distance = 0
        camera.draw(gamebox.from_text(450, 30, str(int(distance*2))+" %", 25, "white"))

        # SLIDE WHEN DOWN ARROW PRESSED --> this is not really useful now...
        if (pygame.K_DOWN in keys or pygame.K_s in keys) and jump is False:
            santa = gamebox.from_image(150, y_pos, slide_stages[frame])
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
        if jump is False and pygame.K_DOWN not in keys:
            santa = gamebox.from_image(150, y_pos, run_stages[frame])
            santa.scale_by(.2)

        # LEVELS
        camera.draw(level_title1)
        level_title1.move(0, -1)
        camera.draw(level_title2)
        level_title2.move(0, -1)
        camera.draw(level_title3)
        level_title3.move(0, -1)
        camera.draw(level_title4)
        level_title4.move(0, -1)

        # Collision detections
        for object in current_level:
            camera.draw(object)
            if y_pos - speed > object.top - 50 and object.left < santa.x < object.right:
                y_pos = object.top - 50
                speed = 0
                jump = False
                if santa.right > object.left and object.top < santa.y < object.bottom:
                    game_over = True
                    play = False

            # CHANGE TO NEXT LEVEL WHEN LEVEL IS OVER
            if object.x < -1500 and level == 4:
                distance = 50
                game_over = True
                play = False
            if object.x < -1500 and level == 3:
                distance = 0
                current_level = level4
                level_title4.y = 50
                level += 1
            if object.x < -1500 and level == 2:
                current_level = level3
                distance = 0
                level_title3.y = 50
                level += 1
            if object.x < -1500 and level == 1:
                current_level = level2
                distance = 0
                level += 1
                level_title2.y = 50

            object.move(-10, 0)

        # CHARACTER'S Y POSITION CHANGES BY THEIR SPEED AND DOWNWARD SPEED INCREASES (GRAVITY)
        y_pos = y_pos - speed
        speed -= 5

        # KEEPS TRACK OF THE ANIMATION FRAMES FOR RUNNING AND SLIDING
        frame += 1
        if frame == 11:
            frame = 0

        # END GAME IF CHARACTER FALLS OFF SCREEN
        if y_pos > 400:
            play = False
            game_over = True

    # DISPLAY END SCREEN WHEN GAME IS OVER
    elif game_over:

        # IF ALL LEVELS HAVE BEEN COMPLETED ALLOW USER TO CHOOSE A LEVEL TO REPLAY
        if distance == 50 and level == 4:
            camera.draw(gamebox.from_text(250, 50, "CONGRATULATIONS", 50, "white"))
            camera.draw(gamebox.from_text(250, 150, "All levels completed!", 50, "white"))
            camera.draw(gamebox.from_text(250, 350, "Replay a level. (Press 1,2 or 3) ", 50, "white"))

            if pygame.K_1 in keys:
                for object in level1:
                    object.move(1500, 0)
                    level_title1.y = 50
                    current_level = level1
                    y_pos = 230
                    speed = 0
                    distance = 0
                    game_over = False
                    play = True
            if pygame.K_2 in keys:
                for object in level2:
                    object.move(1500, 0)
                    level_title2.y = 50
                    current_level = level2
                    y_pos = 230
                    speed = 0
                    distance = 0
                    game_over = False
                    play = True
            if pygame.K_3 in keys:
                for object in level3:
                    object.move(1500, 0)
                    level_title3.y = 50
                    current_level = level3
                    y_pos = 230
                    speed = 0
                    distance = 0
                    game_over = False
                    play = True
            if pygame.K_4 in level4:
                for object in level4:
                    object.move(1500, 0)
                    level_title4.y = 50
                    current_level = level4
                    y_pos = 230
                    speed = 0
                    distance = 0
                    game_over = False
                    play = True

        # IF ALL LEVEL FAILED COMPLETED ALLOW USER TO RETRY CURRENT LEVEL FROM BEGINNING
        else:
            camera.draw(gamebox.from_text(250, 50, "GAME OVER", 100, "white"))
            camera.draw(gamebox.from_text(250, 200, str(int(distance/50*100)) + " %", 100, "white"))
            camera.draw(gamebox.from_text(250, 350, "Press R to restart level", 50, "white"))

            if pygame.K_r in keys:
                if current_level == level1:
                    for object in level1:
                        object.move(3*10*distance, 0)
                    level_title1.y = 50

                if current_level == level2:
                    for object in level2:
                        object.move(distance*3*10, 0)
                    level_title2.y = 50

                if current_level == level3:
                    for object in level3:
                        object.move(distance*3*10, 0)
                    level_title3.y = 50

                if current_level == level4:
                    for object in level4:
                        object.move(distance*3*10, 0)
                    level_title4.y = 50


                y_pos = 230
                speed = 0
                distance = 0
                game_over = False
                play = True

    if not start_screen:
        camera.draw(santa)

    camera.display()


# NOTE: The warning: libpng warning: iCCP: known incorrect sRGB profile prints in the console after the window is closed
# this does not affect the game and is caused by the resizing of the png image.
gamebox.timer_loop(20, tick)
