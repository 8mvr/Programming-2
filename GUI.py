import pygame

pygame.init()
pygame.mixer.init()

# SCREEN
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Pixel Path")
# pygame.display.set_icon(pygame.image.load("icon.png"))
# BACKGROUND MUSIC
pygame.mixer.music.load("pygame/time_for_adventure.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# PLAYER
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

# SCREEN DRAW
def redrawGameWindow():
    screen.fill(("skyblue"))
    pygame.draw.rect(screen, (255, 0, 0), (man.x, man.y, man.width, man.height))
    pygame.draw.rect(screen, ("yellow"), (0, 0, 180, 50))
    font = pygame.font.SysFont("Arial", 72)
    text = font.render('Normal', True, (255, 255, 255))
    screen.blit(text, (0, 0))
    pygame.display.update()

# ASSIGN
man = player(0, 690, 32, 32)
clock = pygame.time.Clock()
jump_sound = pygame.mixer.Sound("pygame/jump.wav")
jump_sound.set_volume(0.1)
running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    # LEFT MOVEMENT
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and  man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False

    # RIGHT MOVEMENT
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1000 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True

    # UP AND DOWN MOVEMENT AND JUMPING
    if not(man.isJump):
        if keys[pygame.K_UP] or keys[pygame.K_w] and man.y > man.vel:
            man.y -= man.vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s] and man.y < 750 - man.height - man.vel:
            man.y += man.vel
        if keys[pygame.K_SPACE]:
            man.isJump = True
            jump_sound.play()
    
    # JUMP HEIGHT
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()
pygame.quit()