# Allison Branch and Tyler Hendricks
# computingIDs: aab4ad and thh4yj

# DESCRIPTION
# A winter themed side scrolling game in which a running character(santa), jumps and slides to avoid obstacles
# (trees, snowmen, etc.)
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

# All file and source code can be found at https://github.com/thh4yj/CS1111FinalProject

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
          gamebox.from_image(1875, 350, "15.png"), gamebox.from_image(1950, 350, "15.png"),
          gamebox.from_image(2000, 350, "15.png"), gamebox.from_image(2075, 350, "15.png"),
          gamebox.from_image(2150, 350, "15.png"), gamebox.from_image(2225, 350, "15.png"),
          gamebox.from_image(2300, 350, "15.png"), gamebox.from_image(2375, 350, "16.png"),
          gamebox.from_image(1875, 215, "14.png"), gamebox.from_image(1950, 215, "15.png"),
          gamebox.from_image(2025, 215, "15.png"), gamebox.from_image(2100, 215, "15.png"),
          gamebox.from_image(2175, 215, "16.png"), gamebox.from_image(2475, 250, "14.png"),
          gamebox.from_image(2550, 250, "15.png"), gamebox.from_image(2625, 250, "15.png"),
          gamebox.from_image(2700, 250, "15.png"), gamebox.from_image(2775, 250, "15.png"),
          gamebox.from_image(2850, 250, "15.png"), gamebox.from_image(2925, 250, "15.png"),
          gamebox.from_image(3000, 250, "15.png")]

level2 = [gamebox.from_image(0, 800, "15.png"), gamebox.from_image(50, 250, "15.png"),
          gamebox.from_image(125, 250, "15.png"), gamebox.from_image(200, 250, "15.png"),
          gamebox.from_image(275, 250, "15.png"), gamebox.from_image(350, 250, "15.png"),
          gamebox.from_image(425, 250, "15.png"), gamebox.from_image(600, 200, "Crate.png"),
          gamebox.from_image(500, 250, "15.png"), gamebox.from_image(575, 250, "15.png"),
          gamebox.from_image(650, 250, "15.png"), gamebox.from_image(725, 250, "16.png"),
          gamebox.from_image(825, 350, "14.png"), gamebox.from_image(900, 350, "15.png"),
          gamebox.from_image(975, 350, "16.png"), gamebox.from_image(1150, 250, "14.png"),
          gamebox.from_image(1225, 250, "16.png"), gamebox.from_image(1400, 150, "14.png"),
          gamebox.from_image(1475, 150, "16.png"), gamebox.from_image(1700, 375, "14.png"),
          gamebox.from_image(1775, 375, "15.png"), gamebox.from_image(1850, 375, "15.png"),
          gamebox.from_image(1925, 375, "16.png"), gamebox.from_image(2150, 275, "14.png"),
          gamebox.from_image(2160, 275, "16.png"), gamebox.from_image(2300, 175, "14.png"),
          gamebox.from_image(2310, 175, "16.png"), gamebox.from_image(2475, 75, "14.png"),
          gamebox.from_image(2485, 75, "16.png"), gamebox.from_image(2475, 350, "14.png"),
          gamebox.from_image(2550, 350, "15.png"), gamebox.from_image(2625, 350, "15.png"),
          gamebox.from_image(2700, 350, "15.png"), gamebox.from_image(2775, 350, "15.png"),
          gamebox.from_image(2850, 350, "15.png"), gamebox.from_image(2925, 350, "15.png"),
          gamebox.from_image(3000, 350, "15.png")]


level3 = [gamebox.from_image(0, 800, "15.png"),
          gamebox.from_image(50, 350, "15.png"), gamebox.from_image(125, 350, "15.png"),
          gamebox.from_image(200, 350, "15.png"), gamebox.from_image(275, 350, "15.png"),
          gamebox.from_image(275, 350, "15.png"), gamebox.from_image(350, 350, "15.png"),
          gamebox.from_image(425, 350, "15.png"), gamebox.from_image(500, 350, "16.png"),
          gamebox.from_image(650, 250, "14.png"), gamebox.from_image(725, 250, "15.png"),
          gamebox.from_image(800, 250, "15.png"), gamebox.from_image(875, 250, "15.png"),
          gamebox.from_image(950, 250, "15.png"), gamebox.from_image(850, 200, "Crate.png"),
          gamebox.from_image(860, 150, "Crate.png"), gamebox.from_image(1025, 250, "15.png"),
          gamebox.from_image(1100, 250, "15.png"), gamebox.from_image(1175, 250, "15.png"),
          gamebox.from_image(1100, 200, "Crate.png"), gamebox.from_image(1110, 150, "Crate.png"),
          gamebox.from_image(1250, 250, "16.png"), gamebox.from_image(1400, 350, "14.png"),
          gamebox.from_image(1475, 350, "15.png"), gamebox.from_image(1550, 350, "15.png"),
          gamebox.from_image(1625, 350, "15.png"), gamebox.from_image(1700, 350, "15.png"),
          gamebox.from_image(1775, 350, "15.png"), gamebox.from_image(1850, 350, "15.png"),
          gamebox.from_image(1925, 350, "15.png"), gamebox.from_image(2000, 350, "16.png"),
          gamebox.from_image(1520, 210, "14.png"), gamebox.from_image(1540, 210, "16.png"),
          gamebox.from_image(1750, 200, "14.png"), gamebox.from_image(1825, 200, "15.png"),
          gamebox.from_image(1900, 200, "15.png"), gamebox.from_image(1975, 200, "16.png"),
          gamebox.from_image(2200, 300, "14.png"), gamebox.from_image(2275, 300, "15.png"),
          gamebox.from_image(2350, 300, "16.png"),
          gamebox.from_image(90 + 2475, 125, "14.png"), gamebox.from_image(150 + 2475, 125, "16.png"),
          gamebox.from_image(170 + 2475, 350, "14.png"), gamebox.from_image(245 + 2475, 350, "15.png"),
          gamebox.from_image(320 + 2475, 350, "15.png"), gamebox.from_image(395 + 2475, 350, "16.png")
          ]


level4 = [gamebox.from_image(90, 125, "14.png"), gamebox.from_image(150, 125, "16.png"),
          gamebox.from_image(170, 350, "14.png"), gamebox.from_image(245, 350, "15.png"),
          gamebox.from_image(320, 350, "15.png"), gamebox.from_image(395, 350, "15.png"),
          gamebox.from_image(470, 350, "16.png"), gamebox.from_image(560, 250, "14.png"),
          gamebox.from_image(625, 250, "16.png"), gamebox.from_image(900, 250, "14.png"),
          gamebox.from_image(975, 250, "16.png"),
          gamebox.from_image(1175, 350, "14.png"), gamebox.from_image(1240, 350, "16.png"),
          gamebox.from_image(1400, 250, "14.png"), gamebox.from_image(1475, 250, "16.png"),
          gamebox.from_image(950, 175, "Snowman.png"), gamebox.from_image(590, 200, "Stone.png"),
          gamebox.from_image(1191, 310, 'Crystal.png'),

          gamebox.from_image(0+1500, 400, '14.png'), gamebox.from_image(75+1500, 400, '15.png'),
          gamebox.from_image(150+1500, 400, '15.png'), gamebox.from_image(225+1500, 400, '15.png'),
          gamebox.from_image(300+1500, 400, '15.png'), gamebox.from_image(375+1500, 400, '15.png'),
          gamebox.from_image(450+1500, 400, '15.png'),
          gamebox.from_image(0+1500, 10, '12.png'), gamebox.from_image(75+1500, 10, '9.png'),
          gamebox.from_image(150+1500, 10, '9.png'), gamebox.from_image(225+1500, 10, '9.png'),
          gamebox.from_image(300+1500, 10, '9.png'), gamebox.from_image(375+1500, 10, '9.png'),
          gamebox.from_image(450+1500, 10, '9.png'),
          gamebox.from_image(270+1500, 345, 'Crate.png'),
          gamebox.from_image(525+1500, 345, 'Crate.png'),
          gamebox.from_image(825+1500, 345, 'Crate.png'),
          ]

level5 = [gamebox.from_image(0, 400, '14.png'), gamebox.from_image(75, 400, '15.png'),
          gamebox.from_image(150, 400, '15.png'), gamebox.from_image(225, 400, '15.png'),
          gamebox.from_image(300, 400, '15.png'), gamebox.from_image(375, 400, '15.png'),
          gamebox.from_image(450, 400, '15.png'), gamebox.from_image(525, 400, '15.png'),
          gamebox.from_image(600, 400, '15.png'), gamebox.from_image(675, 400, '15.png'),
          gamebox.from_image(750, 400, '15.png'), gamebox.from_image(825, 400, '15.png'),
          gamebox.from_image(825, 400, '15.png'), gamebox.from_image(825, 400, '15.png'),
          gamebox.from_image(900, 400, '15.png'), gamebox.from_image(975, 400, '15.png'),
          gamebox.from_image(1050, 400, '15.png'), gamebox.from_image(1125, 400, '15.png'),
          gamebox.from_image(1200, 400, '15.png'), gamebox.from_image(1275, 400, '15.png'),
          gamebox.from_image(1350, 400, '15.png'), gamebox.from_image(1425, 400, '15.png'),
          gamebox.from_image(1500, 400, '15.png'), gamebox.from_image(1575, 400, '16.png'),

          gamebox.from_image(0, 10, '12.png'), gamebox.from_image(75, 10, '9.png'),
          gamebox.from_image(150, 10, '9.png'), gamebox.from_image(225, 10, '9.png'),
          gamebox.from_image(300, 10, '9.png'), gamebox.from_image(375, 10, '9.png'),
          gamebox.from_image(450, 10, '9.png'), gamebox.from_image(525, 10, '9.png'),
          gamebox.from_image(600, 10, '9.png'), gamebox.from_image(675, 10, '9.png'),
          gamebox.from_image(750, 10, '9.png'), gamebox.from_image(825, 10, '9.png'),
          gamebox.from_image(825, 10, '9.png'), gamebox.from_image(825, 10, '9.png'),
          gamebox.from_image(900, 10, '9.png'), gamebox.from_image(975, 10, '9.png'),
          gamebox.from_image(1050, 10, '9.png'), gamebox.from_image(1125, 10, '9.png'),
          gamebox.from_image(1200, 10, '9.png'), gamebox.from_image(1275, 10, '9.png'),
          gamebox.from_image(1350, 10, '9.png'), gamebox.from_image(1425, 10, '9.png'),
          gamebox.from_image(1500, 10, '9.png'), gamebox.from_image(1575, 10, '13.png'),

          gamebox.from_image(270, 345, 'Crate.png'),
          gamebox.from_image(525, 345, 'Crate.png'),
          gamebox.from_image(825, 345, 'Crate.png'), gamebox.from_image(975, 345, 'Crate.png'),
          gamebox.from_image(1125, 345, 'Crate.png'), gamebox.from_image(1275, 345, 'Crate.png')]

# rescale items
snowman = gamebox.from_image(700, 175, "Snowman.png")
snowman.scale_by(.6)
snowman2 = gamebox.from_image(1225, 150, "Snowman.png")
snowman2.scale_by(.75)

for object in level1:
    object.scale_by(.6)
for object in level2:
    object.scale_by(.6)
for object in level3:
    object.scale_by(.6)
for object in level4:
    object.scale_by(.6)
for object in level5:
    object.scale_by(.6)

# create obstacles for levels --> things that santa cannot touch/hit in the game
obstacles = {1: [gamebox.from_image(1600, 300, "Crystal.png"), gamebox.from_image(2050, 150, "Crystal.png"),
                 gamebox.from_image(2100, 150, "Crystal.png"), gamebox.from_image(2150, 150, "Crystal.png")],
             2: [snowman, gamebox.from_image(2485, 25, "Crystal.png"), gamebox.from_image(1810, 315, "Stone.png")],
             3: [gamebox.from_image(975, 200, "Crystal.png"), gamebox.from_image(1025, 200, "Crystal.png"),
                 snowman2, gamebox.from_image(1875, 300, "Stone.png"), gamebox.from_image(1975, 300, "Stone.png"),
                 gamebox.from_image(1540, 170, "Crystal.png")],
             4: [],
             5: []
             }
level_title1 = gamebox.from_text(255, 75, "LEVEL 1", 100, "white")
level_title2 = gamebox.from_text(255, -100, "LEVEL 2", 100, "white")
level_title3 = gamebox.from_text(255, -100, "LEVEL 3", 100, "white")
level_title4 = gamebox.from_text(255, -100, 'LEVEL 4', 100, 'white')
level_title5 = gamebox.from_text(255, -100, 'Level 5', 100, 'white')


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
current_level = level1
level = 1
can_jump = True
slide = False
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
    global can_jump
    global obstacles
    global slide

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
                            'they appear. Use Up or "W" key to jump',
                            'and Down or "S" key to slide.',
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

        # DISPLAY PERCENT OF LEVEL COMPLETED IN TOP RIGHT --> each level has a distance of 250
        # --> may have to adjust this with levels are different lengths
        if level <= 3 and distance > 250:
            distance = 0
        if level <= 3:
            distance += 1
            camera.draw(gamebox.from_text(450, 30, str(int(distance / 250 * 100)) + " %", 25, "white"))
        if level >= 4 and distance > 50:
            distance = 0
        if level >= 4:
            distance += 1/3
            camera.draw(gamebox.from_text(450, 30, str(int(distance / 50 * 100))+" %", 25, "white"))

        # SLIDE WHEN DOWN ARROW PRESSED
        if (pygame.K_DOWN in keys or pygame.K_s in keys) and jump is False:
            santa = gamebox.from_image(150, y_pos, slide_stages[frame])
            santa.scale_by(.2)
            slide = True

        # JUMP WHEN UP ARROW PRESSED --> can only jump when on the ground
        elif (pygame.K_UP in keys or pygame.K_w in keys) and can_jump:
            jump = True
            slide = False
            speed = 30
            santa = gamebox.from_image(150, y_pos, jump_stages[0])
            santa.scale_by(.2)
            keys.clear()

        if jump:
            santa = gamebox.from_image(150, y_pos, jump_stages[jump_count])
            santa.scale_by(.2)
            # To disable single jump, comment the below code:
            jump_count += 1
            if jump_count == 16:
                jump_count = 0
                jump = False
            can_jump = False

        # RUN
        if jump is False and (pygame.K_DOWN not in keys and pygame.K_s not in keys):
            slide = False
            santa = gamebox.from_image(150, y_pos, run_stages[frame])
            santa.scale_by(.2)

        # Create hitboxes for obstacle collision for running/jumping santa or sliding santa
        # --> can view these by drawing
        hitbox = gamebox.from_color(santa.x-15, santa.y-5, "red", 40, 100)
        if slide:
            hitbox = gamebox.from_color(santa.x-10, santa.y+15, "blue", 50, 60)

        # LEVELS
        if current_level is level1:
            camera.draw(level_title1)
            level_title1.move(0, -1)
        if current_level is level2:
            camera.draw(level_title2)
            level_title2.move(0, -1)
        if current_level is level3:
            camera.draw(level_title3)
            level_title3.move(0, -1)
        if current_level is level4:
            camera.draw(level_title4)
            level_title4.move(0, -1)
        if current_level is level5:
            camera.draw(level_title5)
            level_title5.move(0, -1)

        # Path collision
        for object in current_level:

            # only draw objects on screen
            if -75 < object.x < 575:
                camera.draw(object)

            # character can land on paths
            if y_pos - speed > object.top - 50 and y_pos < object.top and object.left < santa.x < object.right:
                y_pos = object.top - 50
                speed = 0
                can_jump = True
                jump = False

            # can't touch path unless walking top of it
            elif hitbox.touches(object, 0, -20):
                game_over = True
                play = False

            # move all the objects
            object.move(-10, 0)

            # CHANGE TO NEXT LEVEL WHEN LEVEL IS OVER --> will need to add for new levels
            if distance >= 50 and level == 5:
                distance = 250
                game_over = True
                play = False
            if distance >= 50 and level == 4:
                current_level = level5
                distance = 0
                level_title5.y = 50
                level += 1
            if object.x < -2500 and level == 3:
                current_level = level4
                distance = 0
                level_title4.y = 50
                level += 1
            if object.x < -2500 and level == 2:
                current_level = level3
                distance = 0
                level_title3.y = 50
                level += 1
            if object.x < -2500 and level == 1:
                current_level = level2
                distance = 0
                level += 1
                level_title2.y = 50

        # detect collisions with obstacles
        for obstacle in obstacles[level]:
            camera.draw(obstacle)
            if hitbox.touches(obstacle, 0, -50):
                    play = False
                    game_over = True
            obstacle.move(-10, 0)

        # KEEP TRACK OF CHARACTER'S Y POSITION, AND CHANGE BY THEIR SPEED, DOWNWARD SPEED INCREASES (GRAVITY)
        y_pos = y_pos - speed
        speed -= 3

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
        if distance >= 250 and level == 5:
            camera.draw(gamebox.from_text(250, 50, "CONGRATULATIONS", 50, "white"))
            camera.draw(gamebox.from_text(250, 150, "All levels completed!", 50, "white"))
            camera.draw(gamebox.from_text(250, 250, "To Replay a Level, ", 50, "white"))
            camera.draw(gamebox.from_text(250, 350, "Type Level Number ", 50, "white"))

            if pygame.K_1 in keys or pygame.K_2 in keys or pygame.K_3 in keys or pygame.K_4 in keys\
                    or pygame.K_5 in keys:

                y_pos = 250
                speed = 0
                distance = 0
                game_over = False
                play = True

                if pygame.K_1 in keys:
                    for object in level1:
                        object.move(2500, 0)
                    for obstacle in obstacles[1]:
                        obstacle.move(2500, 0)
                    level_title1.y = 50
                    current_level = level1
                    level = 1

                if pygame.K_2 in keys:
                    for object in level2:
                        object.move(2500, 0)
                    for obstacle in obstacles[2]:
                        obstacle.move(2500, 0)
                    level_title2.y = 50
                    current_level = level2
                    level = 2

                if pygame.K_3 in keys:
                    for object in level3:
                        object.move(2500, 0)
                    for obstacle in obstacles[3]:
                        obstacle.move(2500, 0)
                    level_title3.y = 50
                    current_level = level3
                    level = 3
                if pygame.K_4 in keys:
                    for object in level4:
                        object.move(1500, 0)
                    level_title4.y = 50
                    current_level = level4
                    level = 4
                if pygame.K_5 in keys:
                    for object in level5:
                        object.move(1500, 0)
                    level_title5.y = 50
                    current_level = level5
                    level = 5

        # IF ALL LEVEL FAILED COMPLETED ALLOW USER TO RETRY CURRENT LEVEL FROM BEGINNING
        else:
            camera.draw(gamebox.from_text(250, 50, "GAME OVER", 100, "white"))
            camera.draw(gamebox.from_text(250, 200, str(int(distance/250*100)) + " %", 100, "white"))
            camera.draw(gamebox.from_text(250, 350, "Press R to restart level", 50, "white"))

            if pygame.K_r in keys:
                if current_level == level1:
                    y_pos = 230
                    for object in level1:
                        object.move(10*distance, 0)
                    level_title1.y = 50
                    for obstacle in obstacles[1]:
                        obstacle.move(10*distance, 0)

                if current_level == level2:
                    y_pos = 150
                    for object in level2:
                        object.move(distance*10, 0)
                    for obstacle in obstacles[2]:
                        obstacle.move(10*distance, 0)
                    level_title2.y = 50

                if current_level == level3:
                    y_pos = 100
                    for object in level3:
                        object.move(distance*10, 0)
                    for obstacle in obstacles[3]:
                        obstacle.move(10*distance, 0)
                    level_title3.y = 50
                if current_level == level4:
                    y_pos = 70
                    for object in level4:
                        object.move(3 * 10 * distance, 0)
                    level_title4.y = 50
                if current_level == level5:
                    y_pos = 300
                    for object in level5:
                        object.move(3 * 10 * distance, 0)
                    level_title5.y = 50

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
