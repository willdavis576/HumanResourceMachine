import hrCmds

step = 0
list = "hello"
tiles = [None]*25
oldTiles = 0
varHeld = None

cmds = hrCmds.hr(list)

for i in range(5):
    match step:
        case 0:
            varHeld = cmds.inbox()
            step = 10
        
        case 10:
            tiles = cmds.copyTo(tiles, False, 0, varHeld)
            step = 20
        
        case 20:
            varHeld = cmds.inbox()
            step = 30
            
        case 30:
            varHeld = cmds.add(tiles, False, 0, varHeld)
            print(varHeld)
            

    print(tiles)
