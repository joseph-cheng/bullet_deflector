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

        self.player = player.Player(width/2, height/2)

##      Stores all of the enemies, currently creates them
        self.enemies = [enemy.Enemy(10, 100, (255,0,0))]
        self.reflected_bullets = []
        self.unreflected_bullets = []

    def update(self):
        current_input_state = self.input_handler.get_current_input_state()

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
