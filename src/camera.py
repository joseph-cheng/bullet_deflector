from vec2 import Vec2

class Camera:
    def __init__(self, pos, w, h):
        self.pos = pos
        self.zoom = 1
        self.screen_size = Vec2(w, h)
        self.size = Vec2(w, h)

        self.target_zoom = 1
        self.target_pos = pos
        self.target_size = Vec2(w, h)


    def update(self):
        if self.pos != self.target_pos:
            self.pos += (self.target_pos - self.pos) * 0.01

        if self.zoom != self.target_zoom:
            self.zoom += (self.target_zoom - self.zoom) * 0.01

        if self.size != self.target_size:
            self.size += (self.target_size - self.size) * 0.01

    def world_to_screen(self, pos):
        return (pos-self.pos) * self.zoom

    def screen_to_world(self, pos):
        return (pos/self.zoom) + self.pos

    def change_zoom(self, new_zoom):
        self.target_zoom = new_zoom

        self.target_size = self.screen_size / self.target_zoom

        self.target_pos = self.pos - (self.target_size - self.size).multiply_vec(Vec2(0.5, 0.5))


