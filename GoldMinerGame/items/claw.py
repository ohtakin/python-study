import pygame

class Claw(pygame.sprite.Sprite):
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    LEFT = -1
    RIGHT = 1
    STOP = 0

    default_offset_x_claw = 40
    to_x = 0
    move_speed = 12
    temp_direction = 0

    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(self.default_offset_x_claw, 0)
        self.position = position
        
        self.direction = self.LEFT
        self.angle_speed = 2.5
        self.angle = 10

    def rotate(self, screen):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        offset_rotated = self.offset.rotate(self.angle)
        # print(offset_rotated)
        self.rect = self.image.get_rect(center=self.position+offset_rotated)
        # print(self.rect)
        pygame.draw.rect(screen, self.RED, self.rect, 1)

    def set_direction(self, direction):
        self.temp_direction = self.direction
        self.direction = direction
        if self.direction == self.STOP:
            self.to_x = self.move_speed

    def set_overflow(self, width, height):
        if self.rect.left < 0 or self.rect.right > width or self.rect.bottom > height:
            self.to_x = -self.move_speed

    def set_init_state(self):
        self.to_x = 0
        self.offset.x = self.default_offset_x_claw
        # self.angle = 10
        self.direction = self.temp_direction

    def update(self, screen):
        if self.direction == self.LEFT:
            self.angle += self.angle_speed
        elif self.direction == self.RIGHT:
            self.angle -= self.angle_speed

        if self.angle > 170:
            self.angle = 170
            self.set_direction(self.RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(self.LEFT)

        self.offset.x += self.to_x
        self.rotate(screen)
        # print(self.angle, self.direction)
        # rect_center = self.position + self.offset
        # self.rect = self.image.get_rect(center=rect_center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, self.RED, self.position, 3)
        pygame.draw.line(screen, self.BLACK, self.position, self.rect.center, 5)
