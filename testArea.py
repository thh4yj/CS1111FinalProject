# Tyler Hendricks
# computingID: thh4yj

import pygame
import gamebox

camera = gamebox.Camera(500, 400)
background = gamebox.from_image(500/2, 400/2, "BG.png")
background.scale_by(.45)

level3 = [gamebox.from_image(-75, 150, "14.png"), gamebox.from_image(-25, 150, "16.png"),
          gamebox.from_image(175, 350, "14.png"), gamebox.from_image(250, 350, "15.png"),
          gamebox.from_image(325, 350, "15.png"), gamebox.from_image(400, 350, "16.png"),
          gamebox.from_image(500, 250, "14.png"), gamebox.from_image(575, 250, "15.png"),
          gamebox.from_image(650, 250, "15.png"), gamebox.from_image(725, 250, "15.png"),
          gamebox.from_image(800, 250, "15.png"), gamebox.from_image(875, 250, "15.png"),
          gamebox.from_image(950, 250, "16.png"), gamebox.from_image(700, 200, "Crate.png"),
          gamebox.from_image(700, 150, "Crate.png"),
          gamebox.from_image(1140, 350, "14.png"), gamebox.from_image(1160, 350, "16.png"),
          gamebox.from_image(1340, 250, "14.png"), gamebox.from_image(1360, 250, "16.png"),
          gamebox.from_image(1540, 125, "14.png"), gamebox.from_image(1600, 125, "16.png"),  #added below
          gamebox.from_image(1610, 350, "14.png"), gamebox.from_image(1685, 350, "15.png"),
          gamebox.from_image(1760, 350, "15.png"), gamebox.from_image(1835, 350, "15.png"),
          gamebox.from_image(1900, 350, "16.png")
          ]

level4 = [gamebox.from_image(75, 125, "14.png"), gamebox.from_image(150, 125, "16.png"),
          gamebox.from_image(170, 350, "14.png"), gamebox.from_image(245, 350, "15.png"),
          gamebox.from_image(320, 350, "15.png"), gamebox.from_image(395, 350, "15.png"),
          gamebox.from_image(470, 350, "16.png"), gamebox.from_image(560, 250, "14.png"),
          gamebox.from_image(625, 250, "16.png"), gamebox.from_image(825, 250, "14.png"),
          gamebox.from_image(890, 250, "16.png"), gamebox.from_image(850, 175, "Snowman.png"),
          gamebox.from_image(590, 200, "Stone.png"), gamebox.from_image(1191, 310, 'Crystal.png'),
          gamebox.from_image(1175, 350, "14.png"), gamebox.from_image(1240, 350, "16.png"),
          gamebox.from_image(1450, 250, "14.png"), gamebox.from_image(1500, 250, "16.png"),
          gamebox.from_image(1540, 125, "14.png"), gamebox.from_image(1560, 125, "16.png")]




# have from -75 to 1560

for object in level4:
    object.scale_by(.6)
for object in level3:
    object.scale_by(.6)

dx = 10

def tick(keys):
    global level4, dx
    camera.clear('black')
    camera.draw(background)

    if pygame.K_u in keys:
        dx += 1
    if pygame.K_i in keys:
        dx -= 1
    if pygame.K_d in keys:
        camera.move(dx, 0)
    if pygame.K_a in keys:
        camera.move(-dx, 0)
    if pygame.K_w in keys:
        camera.move(0, -dx)
    if pygame.K_s in keys:
        camera.move(0, dx)

    for art in level3:
        camera.draw(art)
    camera.display()

gamebox.timer_loop(20, tick)
