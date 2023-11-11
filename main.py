from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()
        self.land.loadMap('map.txt')
        self.hero = Hero((0,0,1),self.land)
        base.camLens.setFov(90)

base = Game()

base.run()


