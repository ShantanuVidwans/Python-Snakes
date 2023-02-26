import pygame


class snake_segment():
    def __init__(self, coor, config):
        self.surf = pygame.image.load("segment.png").convert()
        self.rect = self.surf.get_rect(topleft=coor)
        self.config = config

    def shift(self, direction, curr_direction):
        if direction == "left" and curr_direction != "right":
            return ("left", self.shift_left())
        elif direction == "right" and curr_direction != "left":
            return ("right", self.shift_right())
        elif direction == "up" and curr_direction != "down":
            return ("up", self.shift_up())
        elif direction == "down" and curr_direction != "up":
            return ("down", self.shift_down())
        else:
            return (curr_direction, self.shift(curr_direction, ""))

    def shift_left(self):
        self.rect.centerx -= 10
        if self.rect.midleft[0] - 10 > -1:
            return "safe"
        return "end"

    def shift_right(self):
        self.rect.centerx += 10
        if self.rect.midright[0] + 10 < self.config["screen_width"] + 1:
            return "safe"
        return "end"

    def shift_up(self):
        self.rect.centery -= 10
        if self.rect.midtop[1] - 10 > 29:
            return "safe"
        return "end"

    def shift_down(self):
        self.rect.centery += 10
        if self.rect.midbottom[1] + 10 < self.config["screen_height"] + 1:
            return "safe"
        return "end"
