import os
import pygame
from items import *

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

BLACK = (0, 0, 0)

clock = pygame.time.Clock()
game_font = pygame.font.SysFont("arialrounded", 30)

goal_score = 1500
current_score = 0

game_result = None
total_time = 60

start_ticks = pygame.time.get_ticks()

caught_gemstone = None

def setup_gemstone():
    # small_gold = gemstone.Gemstone(gemstone_images[0], (200, 300))
    small_gold_price, small_gold_speed = 100, 5
    big_gold_price, big_gold_speed = 300, 2
    stone_price, stone_speed = 10, 2
    diamond_price, diamond_speed = 600, 7

    gemstone_group.add(gemstone.Gemstone(gemstone_images[0], (200, 380), small_gold_price, small_gold_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[0], (400, 400), small_gold_price, small_gold_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[0], (600, 450), small_gold_price, small_gold_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[0], (800, 400), small_gold_price, small_gold_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[0], (1150, 380), small_gold_price, small_gold_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[0], (400, 480), small_gold_price, small_gold_speed))
    
    gemstone_group.add(gemstone.Gemstone(gemstone_images[1], (300, 500), big_gold_price, big_gold_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[1], (800, 500), big_gold_price, big_gold_speed))
    
    gemstone_group.add(gemstone.Gemstone(gemstone_images[2], (300, 380), stone_price, stone_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[2], (700, 330), stone_price, stone_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[2], (1000, 480), stone_price, stone_speed))

    gemstone_group.add(gemstone.Gemstone(gemstone_images[3], (900, 420), diamond_price, diamond_speed))
    gemstone_group.add(gemstone.Gemstone(gemstone_images[3], (150, 500), diamond_price, diamond_speed))

def update_score(score):
    global current_score
    current_score += score

def display_score():
    txt_curr_score = game_font.render(f"Current Score: {current_score:,}", True, BLACK)
    screen.blit(txt_curr_score, (50, 20))

    txt_goal_score = game_font.render(f"Goal Score: {goal_score:,}", True, BLACK)
    screen.blit(txt_goal_score, (50, 80))

def display_time(time):
    txt_timer = game_font.render(f"Time: {time}", True, BLACK)
    screen.blit(txt_timer, (1100, 50))

def display_game_over():
    game_font = pygame.font.SysFont("arialrounded", 60)
    txt_game_over = game_font.render(f"{game_result}", True, BLACK)
    rect_game_over = txt_game_over.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
    screen.blit(txt_game_over, rect_game_over)

current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "big_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "stone.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "diamond.png")).convert_alpha()]

gemstone_group = pygame.sprite.Group()
setup_gemstone()

claw_image = pygame.image.load(os.path.join(current_path, "claw.png")).convert_alpha()
claw_sprite = claw.Claw(claw_image, (screen_width // 2, 110))

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            claw_sprite.set_direction(claw_sprite.STOP)

    claw_sprite.set_overflow(screen_width, screen_height)

    if claw_sprite.offset.x < claw_sprite.default_offset_x_claw:    
        claw_sprite.set_init_state()
        if caught_gemstone:
            update_score(caught_gemstone.price)
            gemstone_group.remove(caught_gemstone)
            caught_gemstone = None

    if not caught_gemstone:
        for _gemstone in gemstone_group:
            if pygame.sprite.collide_mask(claw_sprite, _gemstone):
                caught_gemstone = _gemstone
                claw_sprite.to_x = -_gemstone.speed
                break

    if caught_gemstone:
        caught_gemstone.set_position(claw_sprite.rect.center, claw_sprite.angle)

    screen.blit(background, (0, 0))

    gemstone_group.draw(screen)
    claw_sprite.update(screen)
    claw_sprite.draw(screen)

    display_score()

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    display_time(total_time - int(elapsed_time))

    if total_time - int(elapsed_time) <= 0:
        running = False
        if current_score >= goal_score:
            game_result = "Missioin Complete"
        else:
            game_result = "Game Over"

        display_game_over()

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()