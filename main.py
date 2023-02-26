import pygame
from sys import exit
from edges import Edges
from snake import Snake
from food import Food

pygame.init()

config = {
    "screen_width": 800,
    "screen_height": 600,
}

clock = pygame.time.Clock()
screen = pygame.display.set_mode(
    (config["screen_width"], config["screen_height"]))
pygame.display.set_caption("Snakes")

background = pygame.Rect(
    10, 40, config["screen_width"]-20, config["screen_height"]-50)

# Font
text_font = pygame.font.Font(None, 50)
start_game_text_surf = text_font.render("Press Space To Start", False, "Red")
start_game_text_rect = start_game_text_surf.get_rect(
    center=(config["screen_width"]/2, (config["screen_height"]/2)-25))

end_game_text_surf = text_font.render(
    "Game Over!! Press Space to Start Again", False, "Red")
end_game_text_rect = end_game_text_surf.get_rect(
    center=(config["screen_width"]/2, (config["screen_height"]/2)-25))

title_text_surf = text_font.render(
    "Snakes                                                      Score:", False, "Blue")
title_text_rect = title_text_surf.get_rect(topleft=(10, 5))

score = 0


# Edges
GREEN = (255, 30, 70)
BLACK = (0, 0, 0)

edges = Edges(config)
snake = Snake(config)
food = Food(config)


LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
UP = pygame.K_UP
DOWN = pygame.K_DOWN
SPACE = pygame.K_SPACE

curr_direction = "right"

game_end = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(screen, BLACK, background)
    pygame.draw.rect(screen, GREEN, edges.edge_left)
    pygame.draw.rect(screen, GREEN, edges.edge_rigth)
    pygame.draw.rect(screen, GREEN, edges.edge_top)
    pygame.draw.rect(screen, GREEN, edges.edge_bottom)

    screen.blit(title_text_surf, title_text_rect)

    key = pygame.key.get_pressed()
    if key[LEFT]:
        (curr_direction, status) = snake.move("left", curr_direction)
    elif key[RIGHT]:
        (curr_direction, status) = snake.move("right", curr_direction)
    elif key[UP]:
        (curr_direction, status) = snake.move("up", curr_direction)
    elif key[DOWN]:
        (curr_direction, status) = snake.move("down", curr_direction)
    else:
        (curr_direction, status) = snake.move(curr_direction, curr_direction)
    if snake.did_hit_self():
        status = "end"
    if status == "end":
        curr_direction = "right"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            key = pygame.key.get_pressed()
            if key[SPACE]:
                snake = Snake(config)
                score = 0
                break
            pygame.draw.rect(screen, BLACK, background)
            pygame.draw.rect(screen, GREEN, edges.edge_left)
            pygame.draw.rect(screen, GREEN, edges.edge_rigth)
            pygame.draw.rect(screen, GREEN, edges.edge_top)
            pygame.draw.rect(screen, GREEN, edges.edge_bottom)

            screen.blit(title_text_surf, title_text_rect)

            score_text = text_font.render(str(score), False, "Blue")
            screen.blit(score_text, (740, 6))

            for i in snake.body:
                screen.blit(i.surf, i.rect)
            screen.blit(end_game_text_surf, end_game_text_rect)
            pygame.display.update()
            clock.tick(10)

    if snake.did_eat(food):
        score += 1
        food.create_food(snake)
        snake.grow()

    for i in snake.body:
        screen.blit(i.surf, i.rect)
    screen.blit(food.surf, food.rect)

    score_text = text_font.render(str(score), False, "Blue")
    screen.blit(score_text, (740, 6))

    pygame.display.update()
    clock.tick(10)
