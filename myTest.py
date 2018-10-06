from extra.goingto import *
from helper.structs import Point
from extra.graphtraduction import translate
from extra.pathfinding import *
from helper.tile import *
from math import *
def getPath(gameMap, position, destination):
    mapTile = []
    mapContent = []
    print("DESSSS")
    print(destination)
    for i in range(0, len(gameMap.tiles)):
        mapTile.append(list())
        mapContent.append(list())
        for j in range(0, len(gameMap.tiles[0])):
            mapTile[i].append(gameMap.tiles[i][j])
            mapContent[i].append(gameMap.tiles[i][j].TileContent)
    subMapTile = []
    subMapContent = []
    x = -1
    y = -1
    posDepartX = 0
    posDepartY = 0
    posDestX = 0
    posDestY = 0

    for i in range(position.x, destination.x, int(copysign(1,destination.x - position.x))):
        x+=1
        subMapTile.append(list())
        subMapContent.append(list())
        for j in range(position.y, destination.y, int(copysign(1,destination.y - position.y))):
            y +=1
            subMapTile[x].append(mapTile[i][j])
            subMapContent[x].append(mapTile[i][j].TileContent)
            if mapTile[i][j].Position.x == position.x and  mapTile[i][j].Position.y == position.y:
                posDepartX = x
                posDepartY = y
            if mapTile[i][j].Position.x == destination.x and  mapTile[i][j].Position.y == destination.y:
                posDestX = x
                posDestY = y

     


    path = [Point(10,0),Point(11,0)]
    pr1 = goingTo(path)
    path2 = [Point(10,0),Point(11,0),Point(11,1),Point(10,1),Point(10,0)]
    pr2 = goingTo(path2)
    # for e in pr2:
    #     print(e.__str__())

    # print("TEST MAP")
   
    mat2 = [
        [TileContent.Empty,TileContent.Empty,TileContent.Empty],
        [TileContent.Empty,TileContent.Lava,TileContent.Empty],
        [TileContent.Empty,TileContent.Empty,TileContent.Empty]
        ]

    #print("translate : {}".format(translate(subMapContent)))
    #print("findPath : {}".format(find_shortest_path(translate(subMapContent),"{},{}".format(posDepartX, posDepartY),"{},{}".format(posDestX, posDestY))))
    p1rel2 = goingTo(pathStrToPoint(find_shortest_path(translate(subMapContent),"{},{}".format(posDepartX, posDepartY),"{},{}".format(posDestX, posDestY))))

    print(p1rel2)
    return p1rel2
    for e in p1rel2:
        print(e.__str__())

