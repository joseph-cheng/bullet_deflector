import state
import renderer

pygame.init()

state_obj = state.State(800,600)

#TODO: Implement input handling

# main loop
while True:
    state.update()
    state.renderer.render()

