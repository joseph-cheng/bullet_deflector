import renderer
import player

class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.renderer = renderer.Renderer(self.width, self.height)

        self.player = player.Player(width/2, height/2)

    #TODO: implement updating
    def update(self):
        self.player.update()
