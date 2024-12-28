import pygame as pg
from os.path import join  # joins files and folders from system
import random as rand

# general setup
pg.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Space Shooter')
running = True

# surface

# will not be visible unless attached to display surface in game loop
# plain surface
surf = pg.Surface((100, 200))  # creates a rectanble
surf.fill('orange')  # fills rectangle with orange
x = 100

img_path = join('..', 'images')
print(img_path)  # '/' backslash required on linux

# import images
# laser_surface = pg.image.load('../images/laser.png')
# meteor_surface = pg.image.load('../images/meteor.png')
player_surface = pg.image.load(
    join(img_path, 'player.png')).convert_alpha()
# since that not useful we place in center of window using WINDOW_HEIGHT and WINDOWS_WIDTH
player_rect = player_surface.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


star_surface = pg.image.load(join(img_path, 'star.png')).convert_alpha()

meteor_surface = pg.image.load(join(img_path, 'meteor.png')).convert_alpha()
meteor_rect = meteor_surface.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surface = pg.image.load(join(img_path, 'laser.png')).convert_alpha()
laser_rect = laser_surface.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

# rect


player_direction = 1


# puts top left of player_rect at 0, 0 on display surface which is the top left corner.
# player_rect = player_surface.get_frect(topleft=(0, 0))


# could also place in bottom right with the following tuple
#
# player_rect = player_surface.get_frect(
#     bottomright=(WINDOWS_WIDTH - 10, WINDOW_HEIGHT - 10))

num_stars = 20
stars = [(rand.randint(0, WINDOW_WIDTH), rand.randint(0, WINDOW_HEIGHT))
         for _ in range(num_stars)]

while running:
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # draw the game
    # pg.display.flip()  # can update part of the window

    # fill the window with a red color

    # if not filling the backgroud you can see previous frames
    display_surface.fill('cornflowerblue')

    # for i in range(21):   #  this effect looks great but it was not the intent to reload this in the while loop
    #     star_x = rand.randint(0, 1920)
    #     star_y = rand.randint(0, 1080)
    #     display_surface.blit(star_surface, (star_x, star_y))

    # display_surface.blit(meteor_surface, (1920 // 3, 900))
    # display_surface.blit(laser_surface, (1920 // 4, 900))

    # for star_x, star_y in stars:
    #     display_surface.blit(star_surface, (star_x, star_y))

    # Clear Code example

    # x += .2
    # display_surface.blit(player_surface, (x, 150))
    for pos in stars:
        display_surface.blit(star_surface, pos)

    # stops player_rect at right edge of window width
        # if player_rect.right >= WINDOW_WIDTH:
    # elif player_rect.right <= WINDOW_WIDTH:
    #     player_rect.left -= 0.2

    print(player_rect.left)

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)

    # player movement
    player_rect.x += player_direction * 0.4
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1
        # player_rect.left = 100  # sets the left side of the player 100px off left side of surface

    display_surface.blit(player_surface, player_rect)
    # display_surface.blit(surf, (x, 150))

    pg.display.update()  # updateds entire window


pg.quit()
