import os, sys, pygame

from models import human

BASE_DIR = os.path.abspath('')
TREX_PATH = 'assets/1x/trex100.png'
BOMB_PATH = 'assets/1x/bomb50.png'
BOMB_PATH2 = 'assets/1x/bomb50.png'

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

def start():
    pygame.init()
    pygame.display.set_caption('Gorbit')

    clock = pygame.time.Clock()

    size = width, height = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    trex = pygame.image.load(os.path.join(BASE_DIR, TREX_PATH)) # use os.path.join to load files from subdirectories for portability
    trex_rect = trex.get_rect()
    trex_rect.center = (width/2, height/1.5)

    bomb = pygame.image.load(os.path.join(BASE_DIR, BOMB_PATH))
    bomb_rect = bomb.get_rect()
    bomb_rect.center = (25, height/1.5)
    
    braden = 'braden'

    black = 0,0,0

    trex_speed = [0, 2]
    bomb_speed = [3, 0]

    is_jumping = False
    jump_count = 10

    running = True

    def redrawGameWindow():
        screen.fill(black)
        screen.blit(trex, trex_rect) # @blit: block transfer - allows you to copy the contents of one surface to another
        screen.blit(bomb, bomb_rect)
        pygame.display.flip() # updates the screen with everything that's been drawn since the last flip

    def jump():
        nonlocal trex_rect # https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping
        #nonlocal trex_rect
        #trex_speed[1] = -trex_speed[1]
        trex_rect = trex_rect.move(trex_speed)
        #braden = braden + 'a'
        #print(braden)

    while running: # main loop
        #pygame.time.delay(100)
        clock.tick(60)
        #print(clock.get_fps())
        
        for event in pygame.event.get(): # event handling, gets all event from the event queue
            if event.type == pygame.QUIT: # only do something if the event is of type QUIT
                running = False # change the value to False, to exit the main loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # keys = pygame.key.get_pressed()
                    #trex_speed[1] = -trex_speed[1]
                    #trex_rect = trex_rect.move(trex_speed)
                    is_jumping = True
                    #jump()
        #trex_speed[1] = -trex_speed[1]
        #trex_rect = trex_rect.move(trex_speed)
                    #trex_speed[1] = -trex_speed[1]
        if is_jumping: # jump is like a parabola (moving faster at beginning - hangtime at top - then gain speed as you move down)
            if jump_count >= -10:
                neg = -1
                if jump_count < 0:
                    neg = 1 # move character back down
                trex_speed[1] = (jump_count ** 2) * 0.75 * neg
                jump_count -= 1

                print(trex_speed)

                trex_rect = trex_rect.move(trex_speed)
            else:
                is_jumping = False
                jump_count = 10


        bomb_rect = bomb_rect.move(bomb_speed)
        redrawGameWindow()


"""
 # https://www.pygame.org/wiki/tutorials
 # https://www.pygame.org/docs/tut/PygameIntro.html
 # https://www.pygame.org/docs/
 # https://dr0id.bitbucket.io/legacy/pygame_tutorials.html
 # https://realpython.com/pygame-a-primer/
 # https://www.youtube.com/watch?v=UdsNBIzsmlI
 # https://openbookproject.net/thinkcs/python/english3e/pygame.html
 # https://riptutorial.com/pygame/example/18046/event-loop
 # https://petlja.org/biblioteka/r/lekcije/TxtProgInPythonEng/03_pygame-toctree
 # https://pygame-zero.readthedocs.io/en/stable/hooks.html
 # https://stackoverflow.com/questions/44761748/compiling-python-to-webassembly
 # https://github.com/wasmerio/wasmer-python
"""

"""
we erase the screen by filling it with a black RGB color. If you have never worked with animations this 
may seem strange. You may be asking "Why do we need to erase anything, why don't we just move the ball 
on the screen?" That is not quite the way computer animation works. Animation is nothing more than a 
series of single images, which when displayed in sequence do a very good job of fooling the human eye 
into seeing motion. The screen is just a single image that the user sees. If we did not take the time 
to erase the ball from the screen, we would actually see a "trail" of the ball as we continuously draw 
the ball in its new positions.
pygame.event.pump() #https://stackoverflow.com/questions/44254458/pygame-needs-for-event-in-pygame-event-get-in-order-not-to-crash
"""
