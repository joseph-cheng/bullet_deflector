import pygame

#Stores an input state, e.g. what keys or buttons are being pressed
class InputState:

    def __init__(self):
        self.key_code_up = pygame.K_w
        self.key_code_down = pygame.K_s
        self.key_code_left = pygame.K_a
        self.key_code_right = pygame.K_d
        self.key_code_slomo = pygame.K_SPACE

        self.move_up = 0.0
        self.move_down = 0.0
        self.move_left = 0.0
        self.move_right = 0.0
        self.mouse_pos = (0,0)
        self.slomo = False

#Handles all the input events
class InputHandler:

    def __init__(self):
        self.input_state = InputState()

    # Changes input state based on input events
    def input_callback(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == self.input_state.key_code_up:
                    self.input_state.move_up = 1
                if event.key == self.input_state.key_code_down:
                    self.input_state.move_down =1
                if event.key == self.input_state.key_code_right:
                    self.input_state.move_right = 1
                if event.key == self.input_state.key_code_left:
                    self.input_state.move_left = 1
                if event.key == self.input_state.key_code_slomo:
                    self.input_state.slomo = True

            if event.type == pygame.KEYUP:
                if event.key == self.input_state.key_code_up:
                    self.input_state.move_up = 0
                if event.key == self.input_state.key_code_down:
                    self.input_state.move_down = 0
                if event.key == self.input_state.key_code_right:
                    self.input_state.move_right = 0
                if event.key == self.input_state.key_code_left:
                    self.input_state.move_left = 0
                if event.key == self.input_state.key_code_slomo:
                    self.input_state.slomo = False

            if event.type == pygame.MOUSEMOTION:
                self.input_state.mouse_pos = pygame.mouse.get_pos()

    def get_current_input_state(self):
        self.input_callback()
        return self.input_state
