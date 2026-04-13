import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Pixel Path")

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.velY = 0
        self.gravity = 1

def character():
    pygame.draw.rect(screen, ("red"), (man.x, man.y, man.width, man.height))

class obstacle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def obstacles():
    pygame.draw.rect(screen, ("grey"), (obstacle1.x, obstacle1.y, obstacle1.width, obstacle1.height))

def check_collision(player, obstacle):
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
    return player_rect.colliderect(obstacle_rect)

def cloud():
    screen.fill(("#6D4539"))
    cloud1 = pygame.image.load("image/cloud2.png")
    screen.blit(cloud1, (100, 100))
    cloud2 = pygame.image.load("image/cloud2.png")
    screen.blit(cloud2, (450, 50))
    cloud3 = pygame.image.load("image/cloud2.png")
    screen.blit(cloud3, (700, 120))

man = player(100, 600, 32, 32)
obstacle1 = obstacle(500, 600, 100, 10)
clock = pygame.time.Clock()

is_running = True
while is_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        man.x -= man.vel
        if man.x < 0:
            man.x = 0
        if check_collision(man, obstacle1):
            man.x += man.vel
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        man.x += man.vel
        if man.x > 1000 - man.width:
            man.x = 1000 - man.width
        if check_collision(man, obstacle1):
            man.x -= man.vel

    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.velY = -15
    
    man.velY += man.gravity
    man.y += man.velY
    
    if check_collision(man, obstacle1):
        if man.velY > 0:
            man.y = obstacle1.y - man.height
            man.velY = 0
            man.isJump = False
        elif man.velY < 0:
            man.y = obstacle1.y + obstacle1.height
            man.velY = 0
    
    if man.y > 700 - man.height:
        man.y = 700 - man.height
        man.velY = 0
        man.isJump = False
    
    if man.y < 0:
        man.y = 0
        man.velY = 0
    
    
    cloud()
    character()
    obstacles()
    pygame.display.update()
pygame.quit()
