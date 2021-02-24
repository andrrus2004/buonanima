from useful_functions import load_image
from field_all.field_class import Object


class Bullet(Object):
    def __init__(self, creator_pos, mouse_pos):
        super().__init__()
        self.image = load_image("hero/test_img.png")
        self.rect = self.image.get_rect()
        self.rect.x = creator_pos[0]
        self.rect.y = creator_pos[1]

        self.delta_x = mouse_pos[0] - self.rect.x
        self.delta_y = mouse_pos[1] - self.rect.y

        self.speed = 10
        self.sin_x = abs(self.delta_x) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5
        self.sin_y = abs(self.delta_y) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5

        self.speed_x = self.speed * self.sin_x
        self.speed_y = self.speed * self.sin_y

        self.exist = True

    def update(self):
        if self.exist:
            try:
                self.rect.x += round(self.speed_x * self.delta_x / abs(self.delta_x))
                self.rect.y += round(self.speed_y * self.delta_y / abs(self.delta_y))
            except ZeroDivisionError:
                pass
