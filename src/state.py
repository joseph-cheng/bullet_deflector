import renderer
import player
import enemy
import input_handler
import camera
from vec2 import Vec2

class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.camera = camera.Camera(Vec2(0, 0), width, height)
        self.input_handler = input_handler.InputHandler()
        self.renderer = renderer.Renderer(self.width, self.height)
        self.fps = 60

        self.player = player.Player(width/2, height/2)

##      Stores all of the enemies, currently creates them
        self.enemies = [enemy.Enemy(10, 100, (255,0,0))]
        self.reflected_bullets = []
        self.unreflected_bullets = []

        self.regular_updates_per_render = 10
        self.updates_per_render =  self.regular_updates_per_render
        self.updates_since_render = 0
        self.slomo_updates_per_render = 1

    def update(self):
        current_input_state = self.input_handler.get_current_input_state()

        self.camera.update()

        #Increase or decrease the updates per render
        if current_input_state.slomo and self.updates_per_render > self.slomo_updates_per_render:
            self.updates_per_render -= 0.5

        if not(current_input_state.slomo) and self.updates_per_render < self.regular_updates_per_render:
            self.updates_per_render += 0.5

        if current_input_state.slomo and not(current_input_state.slomo_prev):
            self.camera.change_zoom(1.1)

        if current_input_state.slomo_prev and not(current_input_state.slomo):
            self.camera.change_zoom(1)
        self.player.update(current_input_state)
        for enemy in self.enemies:
            enemy.update(self)
            
        for bullet in self.reflected_bullets:
            bullet.collide_with_enemy(self.enemies)          
            bullet.update(self)

        for bullet in self.unreflected_bullets:
            bullet.collide_with_player(self.player)
            bullet.collide_with_deflector(self)
            bullet.update(self)
        
        self.updates_since_render += 1
