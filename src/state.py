import renderer
import player
import enemy
import input_handler

class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height
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

        self.player.update(current_input_state)

        #Increase or decrease the updates per render
        if current_input_state.slomo and self.updates_per_render > self.slomo_updates_per_render:
            self.updates_per_render -= 0.5

        if not(current_input_state.slomo) and self.updates_per_render < self.regular_updates_per_render:
            self.updates_per_render += 0.5

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
