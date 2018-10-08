import renderer
import player
import enemy

class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.renderer = renderer.Renderer(self.width, self.height)

        self.player = player.Player(width/2, height/2)

##      Stores all of the enemies, currently creates them
        self.enemies = [enemy.Enemy(10, 100, (255,0,0)),enemy.Enemy(400, 500, (0,255,0)),enemy.Enemy(800, 400, (0,0,255))]

    #TODO: implement updating
    def update(self):
        self.player.update()
