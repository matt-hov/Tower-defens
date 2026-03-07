import pygame


class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self.image, self.rect)

class MoveSprite(Sprite):
    def __init__(self, center, image, speed, direction):
        super().__init__(center, image)

        self.speed = speed
        self.direction = direction.normalize()

    def updata(self):
        vector =  self.direction * self.speed
        self.rect.move_ip(vector)

window_size = (900,600)
max_fps = 60

window = pygame.Window("tower defence",window_size )
surface = window.get_surface()

clock = pygame.Clock()



center = window_size[0] / 2 , window_size[1] / 2
image = pygame.Surface((50,50))
image.fill("green ")
player = Sprite(center, image)
bullets = []

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            runing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            image = pygame.Surface((6,6))
            image.fill("green")
            center = pygame.Vector2(player.rect.center)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            direction = pos - center
            bullet = MoveSprite( center, image, 7, direction )
            bullets.append(bullet)

    for bullet in bullets:
        bullet.updata()

    surface.fill("red")
    player.render(surface)
    for bullet in bullets:
        bullet.render(surface)
    window.flip()

    clock.tick(max_fps)
    print(bullets)





