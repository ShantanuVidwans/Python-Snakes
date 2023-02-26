from snake_segment import snake_segment


class Snake():
    def __init__(self, config):
        self.body = [
            snake_segment(coor=(100, 100), config=config),
            snake_segment(coor=(110, 100), config=config),
            snake_segment(coor=(120, 100), config=config)
        ]
        self.config = config

    def move(self, direction, curr_direction):
        back = self.body.pop(0)
        back.rect.centerx = self.body[-1].rect.centerx
        back.rect.centery = self.body[-1].rect.centery
        self.body.append(back)
        return back.shift(direction, curr_direction)

    def did_eat(self, food):
        if food.rect.colliderect(self.body[-1]):
            return True
        return False

    def grow(self):
        coor = self.body[-1].rect.topleft
        segment = snake_segment(coor, self.config)
        self.body.append(segment)
