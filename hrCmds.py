#Usable Commands

# inbox
# outbox
# copy from
# copyto
# add
# sub
# bump+
# bump-
# jump
# jump if zero
# jump if neg


class hr:
    def __init__(self, inputList):
        import string
        self.currentList = inputList
        self.listLen = len(self.currentList)
        self.counter = 0
        self.ab = list(string.ascii_lowercase) #import alphabet
        self.ab.insert(0,0)
        self.outputString = ""
    
    def inbox(self):
        if self.counter < self.listLen:
            self.counter += 1
            return self.currentList[self.counter -1]
        
    def output(self, var):
        self.outputString = self.outputString + var
        
    def finish(self):
        return self.outputString
        
    def copyFrom(self, tiles, ni, whatTile):
        if ni == False: #var
            return tiles[whatTile] 
        if ni == True: #index
            return tiles[tiles[whatTile]]
        
    def copyTo(self, tiles, ni, whatTile, varHeld):
        if ni == False: #var
            tiles[whatTile] = varHeld
            return tiles
        if ni == True: #index
            tiles[tiles[whatTile]] = varHeld
            return tiles
    
    def add(self, tiles, ni, whatTile, varHeld):
        if ni == False: #var
            if isinstance(varHeld, str) == False: #number
                return tiles[whatTile] + varHeld
            if isinstance(varHeld, str) == True and isinstance(tiles[tiles[whatTile]],str) == True: #string
                return self.ab.index(varHeld) + self.ab.index(tiles[tiles[whatTile]])
            
        if ni == True and isinstance(varHeld, str) == False: #index
            return tiles[tiles[whatTile]] + varHeld
        
    def sub(self, tiles, ni, whatTile, varHeld):
        if ni == False: #var
            if isinstance(varHeld, str) == False: #number
                return varHeld - tiles[whatTile]
            if isinstance(varHeld, str) == True and isinstance(tiles[tiles[whatTile]],str) == True: #string
                return self.ab.index(varHeld) - self.ab.index(tiles[tiles[whatTile]])

        if ni == True and isinstance(varHeld, str) == False: #index
            return varHeld - tiles[tiles[whatTile]]
        
    def bumpP(self, tiles, ni, whatTile):
        if ni == False: #var
            tiles[whatTile] += 1
            return tiles, tiles[whatTile]
        if ni == True: #index
            tiles[tiles[whatTile]] += 1
            return tiles, tiles[tiles[whatTile]]
        
    def bumpS(self, tiles, ni, whatTile):
        if ni == False: #var
            tiles[whatTile] -= 1
            return tiles, tiles[whatTile]
        if ni == True: #index
            tiles[tiles[whatTile]] -= 1
            return tiles, tiles[tiles[whatTile]]

    def jump(self, num):
        return num
    
    def jumpIfZero(self, num, varHeld):
        if varHeld == 0:
            return num
    
    def jumpIfNeg(self, num, varHeld):
        if varHeld < 0:
            return num
        