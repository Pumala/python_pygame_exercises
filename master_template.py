import pygame
import random
# using the time module
import time
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
ENTER = 13

def sqr(x):
    return x * x

def distance(thing1, thing2):
    return math.sqrt(sqr(thing1.x - thing2.x) + sqr(thing1.y - thing2.y))

class Character(object):

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Hero(Character):
    def __init__(self):
        self.name = "hero"
        self.x = 240
        self.y = 240
        self.width = 32
        self.height = 32
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.image.load("images/hero.png")

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if (self.x + (self.width * 2) >= width):
            self.speed_x = -5
            print "I am 1"
        if (self.x - self.width) <= 0:
            self.speed_x = 5
            print "I am 2"
        if (self.y + (self.height * 2) >= height):
            self.speed_y = -5
            print "I am 3"
        if self.y - self.height <= 0:
            self.speed_y = 5
            print "I am 4"

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            # activate the cooresponding speeds
            # when an arrow key is pressed down
            if event.key == KEY_DOWN:
                self.speed_y = 5
            elif event.key == KEY_UP:
                self.speed_y = -5
            elif event.key == KEY_LEFT:
                self.speed_x = -5
            elif event.key == KEY_RIGHT:
                self.speed_x = 5
        if event.type == pygame.KEYUP:
            # deactivate the cooresponding speeds
            # when an arrow key is released
            if event.key == KEY_DOWN:
                self.speed_y = 0
            elif event.key == KEY_UP:
                self.speed_y = 0
            elif event.key == KEY_LEFT:
                self.speed_x = 0
            elif event.key == KEY_RIGHT:
                self.speed_x = 0

    def collides(self, monster):
        return distance(self, monster) < 32

class Monster(Character):
    def __init__(self):
        self.name = "monster"
        self.x = 100
        self.y = 100
        self.width = 32
        self.height = 30
        self.speed_x = 5
        self.speed_y = 0
        self.image = pygame.image.load("images/monster.png")
        self.dir_change_countdown = 120

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if (self.x + (self.width * 2) >= width):
            self.x = self.width
            print "monster 1"
        if (self.x - (self.width - 2) <= 0):
            self.x = width - (self.width * 2)
            print "monster 2"
        if self.y + (self.height * 2) >= height:
            self.y = self.height
            print "monster 3"
        if self.y - self.height <= 0:
            self.y = height - (self.height * 2)
            print "monster 4"

        self.maybe_change_direction()

    def maybe_change_direction(self):
        self.dir_change_countdown -= 1
        if self.dir_change_countdown <= 0:
            self.dir_change_countdown = 120
            self.change_direction()

    def change_direction(self):
        randNum = random.randint(0, 3)
        self.speed_x = 0
        self.speed_y = 0
        # print randNum
        if randNum == 0:
            self.speed_x = 5
            self.speed_y = 0
        elif randNum == 1:
            self.speed_x = -5
            self.speed_y = 0
        elif randNum == 2:
            self.speed_y = 5
            self.speed_x = 0
        else:
            self.speed_y = -5
            self.speed_x = 0

    def respawn(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

def main():
    # declare the size of the canvas
    width = 512
    height = 480

    # initialize the pygame framework
    pygame.init()

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
    win_sound = pygame.mixer.Sound("sounds/win.wav")
    #  when you call time.time() it gets the time of now
    # now = time.time()
    # countdown for when to perform the action of changing directions
    # time_til_dir_change = now + 2

    # create an instance of monster and hero
    monster = Monster()
    hero = Hero()

    # game loop
    game_over = False
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            # pass in the event
            hero.process_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == ENTER:
                    game_over = False
                    print "Starting over...."
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        if not game_over:
            hero.update(width, height)
            monster.update(width, height)
            if hero.collides(monster):
                win_sound.play()
                game_over = True
                monster.respawn(width, height)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        screen.blit(background_image, (0, 0))
        hero.render(screen)

        if game_over:
            font = pygame.font.Font(None, 35)
            text = font.render("Hit RETURN to play again!", True, (100, 0, 150))
            screen.blit(text, (45, 250))
        else:
            monster.render(screen)


        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()

# for later add in the collision logic
# first, import math at the top of the page
# create a function using the squareroot logic

# now = time.time()
# if now >= time_til_dir_change:
#     #  perform the direction change
#     time_til_dir_change = now + 2
