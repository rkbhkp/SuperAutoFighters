import pygame
import random

# init pygame
pygame.init()

# create screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# set name
pygame.display.set_caption("Super Auto Fighters")
icon = pygame.image.load("spears.png")
pygame.display.set_icon(icon)

# player 
playerImg = pygame.image.load('greek.png')
image_width, image_height = playerImg.get_size()
image_width, image_height = image_width/4, image_height/4
playerImg = pygame.transform.scale(playerImg, (image_width, image_height))
playerX = (screen_width - image_width) // 2
playerY = (screen_height - image_height) // 2
playerX_change = 0

# enemy 
enemyImg = pygame.image.load('army.png')
enemy_width, enemy_height = enemyImg.get_size()
enemy_width, enemy_height = image_width/4, image_height/4
enemyImg = pygame.transform.scale(enemyImg, (enemy_width, enemy_height))
enemyX = (screen_width - image_width) // 4
enemyY = (screen_height - image_height) // 4
enemyX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))
def enemy(x,y):
    screen.blit(enemyImg, (x, y))
  

running = True

while running:
    screen.fill((0,100,40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = .3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
    enemyX += random.uniform(-0.3, 0.3)
    # Ensure the image stays within the screen boundaries
    playerX = max(0, min(playerX, screen_width - image_width))
    playerY = max(0, min(playerY, screen_height - image_height))
    
    enemyX = max(0, min(enemyX, screen_width - enemy_width))
    penemyY = max(0, min(enemyY, screen_height - enemy_height))


    playerX += playerX_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update() 