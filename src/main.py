import pygame

import state
import renderer

pygame.init()

clock = pygame.time.Clock()

state_obj = state.State(800,600)

#TODO: Implement input handling


# main loop
while True:

    for x in range(int(state_obj.updates_per_render)):
        state_obj.update()

    state_obj.renderer.render(state_obj)

    #Cap the framerate
    clock.tick(state_obj.fps)

