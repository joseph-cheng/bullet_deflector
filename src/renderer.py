import pygame

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((self.width, self.height))

    def render(self, state_obj):
        self.screen.fill((255,255,255))

        state_obj.player.render(self.screen)

        pygame.display.update()

