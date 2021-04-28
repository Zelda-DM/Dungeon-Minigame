# --- Imports ---
import pygame
import os
import random
# --- Screen Dimensions ---
SCR_WIDTH = 1020
SCR_HEIGHT = 510
# --- Colors ---
WHITE = [240, 240, 240]
# --- Game Constants ---
FPS = 60
score = 0
lives = 3
# --- Fonts ---
pygame.font.init()
TNR_FONT = pygame.font.SysFont('Times_New_Roman', 27)
# --- Player Variables ---
playerX = 120
playerY = 100
# --- Dictionaries/Lists ---
images = {}
enemy_list = []
bullets = []
# --- Classes ---
class Enemy:
    def __init__(self):
        self.x = random.randint(600, 1000)
        self.y = random.randint(8, 440)
        self.moveX = 0
        self.moveY = 0

    def move(self):
        if self.x > playerX:
            self.x -= 0.7
        
        if self.x <= 215:
            self.x = 215
            enemy_list.remove(enemy)
            for i in range(1):
                new_enemy = Enemy()
                enemy_list.append(new_enemy)

    def draw(self):
        screen.blit(images['l_zombie'], (self.x, self.y))
# --- Functions --
def load_zombies():
    for i in range(8):
        new_enemy = Enemy()
        enemy_list.append(new_enemy)
def clip(value, lower, upper):
    return min(upper, max(value, lower))
def load_images():
    path = 'Desktop/Files/Dungeon Minigame/'
    filenames = [f for f in os.listdir(path) if f.endswith('.png')]
    for name in filenames:
        imagename = os.path.splitext(name)[0]
        images[imagename] = pygame.image.load(os.path.join(path, name))
def main_menu():
    screen.blit(images['background'], (0, 0))
    start_button = screen.blit(images['button'], (420, 320))
    onclick = False
    while True:
        mx, my = pygame.mouse.get_pos()
        if start_button.collidepoint((mx, my)):
            if onclick:
                game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                onclick = True
        clock.tick(FPS)
        pygame.display.update()
def game(): 

    load_zombies()

    while True:

        global playerX, playerY, score, lives, enemy

        screen.blit(images['background2'], (0, 0))
        score_text = TNR_FONT.render('Score: ' + str(score), True, WHITE)
        lives_text = TNR_FONT.render('Lives: ', True, WHITE)
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (840, 20))
        screen.blit(images['r_knight'], (playerX, playerY))

        heart_images = ["triple_empty_heart", "single_heart", "double_heart", "triple_heart"]
        lives = clip(lives, 0, 3)
        screen.blit(images[heart_images[lives]], (920, 0))

        if lives == 0:
            main_menu()

        for enemy in enemy_list:
            enemy.move()
            enemy.draw()
            if enemy.x == 215:
                lives -= 1
    
        onpress = pygame.key.get_pressed()

        Y_change = 0
        if onpress[pygame.K_w]:
            Y_change -= 5
        if onpress[pygame.K_s]:
            Y_change += 5
        playerY += Y_change

        X_change = 0
        if onpress[pygame.K_a]:
            X_change -= 5
        if onpress[pygame.K_d]:
            X_change += 5
        playerX += X_change

        playerX = clip(playerX, -12, 100)
        playerY = clip(playerY, -15, 405)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
        clock.tick(FPS)
        pygame.display.update()
# --- Main ---
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption('Dungeon Minigame')
load_images()
main_menu()
