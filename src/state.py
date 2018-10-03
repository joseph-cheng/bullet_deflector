import renderer

class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.renderer = renderer.Renderer(self.width, self.height)

    #TODO: implement updating
    def update(self):
        pass
