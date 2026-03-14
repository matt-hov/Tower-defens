from random import randint
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
enemies = []
score = 0

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


    if randint(0,100) <= 5:
        image = pygame.Surface((20,20))
        image.fill("#43bccc")
        center = pygame.Vector2(player.rect.center)

        r = randint(1, 4)
        if r == 1:
            pos = pygame.Vector2(randint(0 , window_size[0]),-100)
        if r == 2:
            pos = pygame.Vector2(window_size[0] +100, randint(0,window_size[1]))
        elif r == 3:
            pos = pygame.Vector2(randint(0 , window_size[0]), window_size[1]+100)
        else:
            pos = pygame.Vector2(-100,randint(0 , window_size[1]))

        direction = center - pos
        enemy = MoveSprite(pos, image, randint(100,400) / 100, direction)
        enemies.append(enemy)

    for bullet in bullets:
        bullet.updata()

    for enimy in enemies:
        enimy.updata()

    surface.fill("blue")
    player.render(surface)

    for bullet in bullets:
        bullet.render(surface)
    for enimy in enemies:
        enimy.render(surface)
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                score += 1
                bullets.remove(bullet)
                enemies.remove(enemy)
                break


    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            score = 0
            enemies.clear()
            bullets.clear()
            break

    window.flip()

    clock.tick(max_fps)
    print(bullets)







