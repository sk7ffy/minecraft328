import pickle
class MapManager:
    def __init__(self):
        self.model2 = 'block2'
        self.texture2 = 'block2.png'
        self.model = 'block'
        self.texture = 'block3.png'
        
        self.color = (0.2,0.2,0.35,2)
        self.addNew()
    def addNew(self):   
        
        """ створюємо основу для карти
        """
        self.land = render.attachNewNode('Land')
    
    def addBlock(self,pos):
        block = loader.loadModel(self.model)
        block_texture = loader.loadTexture(self.texture)
    
        block.setTexture(block_texture)
        block.setPos(pos)
        block.setColor(self.color)
        block.setTag('at',str(pos))
        block.reparentTo(self.land)

    def addBlock2(self,pos):
        block = loader.loadModel(self.model)
        block_texture = loader.loadTexture('block.png')

        block.setTexture(block_texture)
        block.setPos(pos)
        block.setColor(self.color)
        block.setTag('at',str(pos))
        block.reparentTo(self.land)

    def addBlock3(self,pos):
        block = loader.loadModel(self.model)
        block_texture = loader.loadTexture('cobble2.png')

        block.setTexture(block_texture)
        block.setPos(pos)
        block.setColor(self.color)
        block.setTag('at',str(pos))
        block.reparentTo(self.land)

    
    

    def delBlock(self,position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self,pos):
        x,y,z = self.findHighestEmpty(pos)
        pos = x,y,z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def buildBlock(self, pos):
        x, y, z = pos
        new_pos = self.findHighestEmpty(pos)
        if new_pos[2] < z + 1:
            self.addBlock(new_pos)

    def buildBlock2(self, pos):
        x, y, z = pos
        new_pos = self.findHighestEmpty(pos)
        if new_pos[2] < z + 1:
            self.addBlock(new_pos)

    def buildBlock3(self, pos):
        x, y, z = pos
        new_pos = self.findHighestEmpty(pos)
        if new_pos[2] < z + 1:
            self.addBlock(new_pos)
        

        

        


    def loadMap(self,filename):
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for number in line:
                    for z in range(int(number)+1):
                        self.addBlock((x,y,z))
                    x += 1
                y += 1
            


    def saveMap(self):
        blocks = self.land.getChildren()
        with open('map.dat',"wb") as file:
            pickle.dump(len(blocks), file)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, file)

    def clear(self):
        self.land.removeNode()
        self.addNew()
        
    def loadLand(self):
        self.clear()
        with open ('map.dat','rb') as file:
            lenght = pickle.load(file)

            for i in range(lenght):
                pos = pickle.load(file)
                self.addBlock(pos)


    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
        
    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1

        while not self.isEmpty((x,y,z)):
            z += 1

        return (x, y, z)