import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Character(object):
    def __init__(self, x, y):
        self.name = "<undefined>"
        self.x = x
        self.y = y
        self.speed_x = 2
        self.speed_y = 2

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Hero(Character):
    def __init__(self, x, y):
        self.name = "hero"
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.speed_x = 0
        self.speed_y = 0

    # def update(self):
    #     self.x += self.speed_x
    #     self.y += self.speed_y

class Monster(Character):
    def __init__(self, x, y):
        self.name = "monster"
        self.x = x
        self.y = y
        self.width = 32
        self.height = 30
        self.speed_x = 5
        self.speed_y = 0

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)
    monster_x = 410
    monster_y = 20
    hero_x = 240
    hero_y = 240

    # initialize the pygame framework
    pygame.init()

    # create an instance of monster and hero
    monster = Monster(monster_x, monster_y)
    hero = Hero(hero_x, hero_y)

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # hero


    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background_image = pygame.image.load("images/background.png").convert_alpha()
    hero_image = pygame.image.load("images/hero.png").convert_alpha()
    monster_image = pygame.image.load("images/monster.png").convert_alpha()
    change_dir_countdown = 120

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYDOWN and (hero.x >= 0 or hero.x <= 450):

                # print "Hello, I'm inside!!"

                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.speed_y = 5
                elif event.key == KEY_UP:
                    hero.speed_y = -5
                elif event.key == KEY_LEFT:
                    hero.speed_x = -5
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = 0
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            randNum = random.randint(0, 3)
            monster.speed_x = 0
            monster.speed_y = 0
            # print randNum
            if randNum == 0:
                monster.speed_x = 5
            elif randNum == 1:
                monster.speed_x = -5
            elif randNum == 2:
                monster.speed_y = 5
            else:
                monster.speed_y = -5
        #  monster speed
        if (monster.x + (monster.width * 2) >= width):
            monster.x = monster.width
            print "monster 1"
        if (monster.x - (monster.width - 2) <= 0):
            monster.x = width - (monster.width * 2)
            print "monster 2"
        if monster.y + (monster.height * 2) >= height:
            monster.y = monster.height
            print "monster 3"
        if monster.y - monster.height <= 0:
            monster.y = height - (monster.height * 2)
            print "monster 4"

        # best monster vs
        # if (monster.x + (monster.width * 2) >= width):
        #     monster.x = monster.width
        #     print "monster 1"
        # if (monster.x - (monster.width - 2) <= 0):
        #     monster.x = width - (monster.width * 2)
        #     print "monster 2"
        # if monster.y + (monster.height * 2) >= height:
        #     monster.y = monster.height
        #     print "monster 3"
        # if monster.y - monster.height <= 0:
        #     monster.y = height - (monster.height * 2)
        #     print "monster 4"

        # if (monster.x + monster.speed_x >= width):
        #     monster.x = 0
        # if (monster.x + monster.speed_x <= 0):
        #     monster.x = width
        # if (monster.y + monster.speed_y >= height):
        #     monster.y = 0
        # if (monster.y + monster.speed_y <= 0):
        #     monster.y = height
        # hero speed
        if (hero.x + (hero.width * 2) >= width):
            hero.speed_x = -5
            print "I am 1"
        if (hero.x - hero.width) <= 0:
            hero.speed_x = 5
            print "I am 2"
        if (hero.y + (hero.height * 2) >= height):
            hero.speed_y = -5
            print "I am 3"
        if hero.y - hero.height <= 0:
            hero.speed_y = 5
            print "I am 4"


        # better version
        # if (hero.x + (hero.width * 2) >= width):
        #     hero.speed_x = -5
        #     print "I am 1"
        # if (hero.x - hero.width) <= 0:
        #     hero.speed_x = 5
        #     print "I am 2"
        # if (hero.y + (hero.height * 2) >= height):
        #     hero.speed_y = -5
        #     print "I am 3"
        # if hero.y - hero.height <= 0:
        #     hero.speed_y = 5
        #     print "I am 4"




        # if (hero.x + (hero.width) >= width):
        #     hero.x = hero.width
        #     print "I am 1"
        # if (hero.x + (hero.width) <= 0):
        #     hero.x = width - hero.width
        #     print "I am 2"
        # if (hero.y + (hero.height) >= height):
        #     hero.y = hero.height
        #     print "I am 3"
        # if (hero.y + (hero.height) <= 0):
        #     hero.y = height - hero.width
        #     print "I am 4"

        # monster.speed_x += 5


        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        hero.update()
        monster.update()

        screen.blit(background_image, (0, 0))

        # hard coded hero's position
        # will come back and change to make flexible
        screen.blit(hero_image, (hero.x, hero.y))
        screen.blit(monster_image, (monster.x, monster.y))

        # fill background color
        # screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
