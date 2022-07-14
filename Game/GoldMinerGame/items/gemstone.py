import pygame
import math
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position, price, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price
        self.speed = speed

    def set_position(self, position, angle):
        r = self.rect.size[0] // 2
        red_angle = math.radians(angle)
        to_x = r * math.cos(red_angle)
        to_y = r * math.sin(red_angle)

        self.rect.center = (position[0] + to_x, position[1] + to_y)

