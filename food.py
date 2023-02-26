import pygame
import random
import time


class Food():
    def __init__(self, config):
        self.config = config
        self.surf = pygame.image.load("food.png").convert()
        self.rect = self.surf.get_rect(topleft=self.get_rand_coor())

    def get_rand_coor(self):
        random.seed(time.time())
        x = (random.randint(10, self.config["screen_width"] - 10) // 10) * 10
        y = (random.randint(10, self.config["screen_height"] - 40) // 10) * 10
        return (x, y)

    def create_food(self, snake):
        self.rect.topleft = self.get_rand_coor()
        # while self.rect.collidelist(snake.body):
        #     self.rect.topleft = self.get_rand_coor()
