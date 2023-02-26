import pygame


class Edges():
    def __init__(self, config):
        self.edge_left = pygame.Rect(0, 0, 10, config["screen_height"])
        self.edge_rigth = pygame.Rect(
            config["screen_width"]-10, 0, 10, config["screen_height"])
        self.edge_top = pygame.Rect(0, 0, config["screen_width"], 40)
        self.edge_bottom = pygame.Rect(
            0, config["screen_height"] - 10, config["screen_width"], 10)

    # def get_rect_list(self):
    #     return [self.edge_left, self.edge_rigth, self.edge_top, self.edge_bottom]
