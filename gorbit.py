import os, sys, pygame

from models import human

BASE_DIR = os.path.abspath('')
TREX_PATH = 'assets/1x/trex100.png'
BOMB_PATH = 'assets/1x/bomb50.png'

def start():
    pygame.init()

    size = width, height = (500, 500)
    screen = pygame.display.set_mode(size)

    trex = pygame.image.load(os.path.join(BASE_DIR, TREX_PATH)) # use os.path.join to load files from subdirectories for portability
    trex_rect = trex.get_rect()
    trex_rect.center = (width/2, height/2)

    bomb = pygame.image.load(os.path.join(BASE_DIR, BOMB_PATH))
    bomb_rect = bomb.get_rect()
    bomb_rect.center = (25, height/2)
    

    black = 0,0,0

    trex_speed = [0, 1]
    bomb_speed = [1, 0]

    running = True
    init = True

    def reload():
        screen.fill(black)
        screen.blit(trex, trex_rect)
        screen.blit(bomb, bomb_rect)
        pygame.display.flip()

    while running: # main loop
        #print('you\'ve entered gorbit')
        for event in pygame.event.get(): # event handling, gets all event from the event queue
            if event.type == pygame.QUIT: # only do something if the event is of type QUIT
                running = False # change the value to False, to exit the main loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    trex_speed[1] = -trex_speed[1]
                    for _ in range(75):
                        pygame.event.pump() #https://stackoverflow.com/questions/44254458/pygame-needs-for-event-in-pygame-event-get-in-order-not-to-crash
                        trex_rect = trex_rect.move(trex_speed)
                        reload()
                    trex_speed[1] = -trex_speed[1]
                    for _ in range(75):
                        pygame.event.pump()
                        trex_rect = trex_rect.move(trex_speed)
                        reload()

        bomb_rect = bomb_rect.move(bomb_speed)
        reload()

        if init:
            reload()
            init = False


"""
 # https://www.pygame.org/wiki/tutorials
 # https://www.pygame.org/docs/tut/PygameIntro.html
 # https://www.pygame.org/docs/
 # https://dr0id.bitbucket.io/legacy/pygame_tutorials.html
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
"""
