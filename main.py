import pygame


class Sprite:
    def __int__(self, center, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self.image, self.rect)


window_size = (900,600)
max_fps = 60

window = pygame.Window("tower defence",window_size )
surface = window.get_surface()

clock = pygame.Clock()

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            runing = False


    surface.fill("black")
    ...
    window.flip()

    clock.tick(max_fps)
    print(clock.get_fps())



