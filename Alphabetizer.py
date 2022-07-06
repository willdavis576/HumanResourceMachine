import hrCmds

step = 0
list = "hello"
expectedOutput = "hello"
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
            cmds.output(varHeld)
            step = 20
 
          
        
       
            

print(tiles)
print("expected output ", expectedOutput, "you produced", cmds.finish())