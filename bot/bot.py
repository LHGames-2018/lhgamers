from helper import *
from bot.dijkstra import shortestPath
from extra.graphtraduction import translate
class Bot:
    def __init__(self):
        self.goingToHouse = False
        self.previousPosition = None
        self.previousDirection = None

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        if(gameMap.getTileAt(self.PlayerInfo.Position+Point(1,0)).TileContent == TileContent.Player):
            return create_attack_action(Point(1,0))
        elif(gameMap.getTileAt(self.PlayerInfo.Position+Point(-1,0)).TileContent == TileContent.Player):
            return create_attack_action(Point(-1,0))
        elif(gameMap.getTileAt(self.PlayerInfo.Position+Point(0,1)).TileContent == TileContent.Player):
            return create_attack_action(Point(0,1))
        elif(gameMap.getTileAt(self.PlayerInfo.Position+Point(0,-1)).TileContent == TileContent.Player):
            return create_attack_action(Point(0,-1))
        if self.PlayerInfo.CarriedResources >= self.PlayerInfo.CarryingCapacity:
            self.goingToHouse = True
        res = list()
        for x in range(gameMap.xMin,gameMap.xMax):
            for y in range(gameMap.yMin, gameMap.yMax):
                if gameMap.getTileAt(Point(x,y)).TileContent == TileContent.Resource:
                    res.append(Point(x,y))
                elif gameMap.getTileAt(Point(x,y)).TileContent == TileContent.House:
                    house = Point(x,y)
        if not self.goingToHouse:
            res.sort(key=lambda p: Point.Distance(p, self.PlayerInfo.Position))
            if not len(res):
                self.goingToHouse=True
                return
            index = 0
            pathFound = False
            while not pathFound:
                if index >= len(res):
                    self.goingToHouse = True
                    return
                closestRes = res[index]

                path = list()
                if gameMap.getTileAt(closestRes-Point(1,0)) and gameMap.getTileAt(closestRes-Point(1,0)).TileContent == TileContent.Empty:
                    path = shortestPath(translate(gameMap.tiles), self.PlayerInfo.Position, (closestRes-Point(1,0)))
                    print(path)
                elif gameMap.getTileAt(closestRes-Point(0,1)) and gameMap.getTileAt(closestRes-Point(0,1)).TileContent == TileContent.Empty and len(path) == 0 :
                    path = shortestPath(translate(gameMap.tiles), self.PlayerInfo.Position, (closestRes-Point(0,1)))
                elif gameMap.getTileAt(closestRes+Point(1,0)) and gameMap.getTileAt(closestRes+Point(1,0)).TileContent == TileContent.Empty and len(path) == 0:
                    path = shortestPath(translate(gameMap.tiles), self.PlayerInfo.Position, (closestRes+Point(1,0)))
                    print(path)
                elif gameMap.getTileAt(closestRes+Point(0,1)) and gameMap.getTileAt(closestRes+Point(0,1)).TileContent == TileContent.Empty and len(path) == 0:
                    path = shortestPath(translate(gameMap.tiles), self.PlayerInfo.Position, (closestRes+Point(0,1)))
                else:
                    index += 1
                if len(path) > 0:
                    pathFound = True
                else:
                    index += 1

                


            # direction = closestRes - self.PlayerInfo.Position
            direction = path[1] - self.PlayerInfo.Position
            print(closestRes)
            print(self.PlayerInfo.Position)
            print(direction)
            print(self.PlayerInfo.TotalResources)
            print(self.PlayerInfo.CarriedResources)
            collectDir = closestRes - self.PlayerInfo.Position
            if Point.Distance(self.PlayerInfo.Position, closestRes) <= 1:
                if(collectDir.x !=0):
                    dirX = int(collectDir.x/abs(collectDir.x))
                else:
                    dirX = 0
                if(collectDir.y != 0):
                    dirY = int(collectDir.y/abs(collectDir.y))
                else:
                    dirY = 0
                if(dirX ==0 and dirY==0):
                    self.goingToHouse = True
                return create_collect_action(Point(dirX, dirY))
            
        else:
            path = shortestPath(translate(gameMap.tiles), self.PlayerInfo.Position, self.PlayerInfo.HouseLocation)
            if len(path)>1:
                if(self.previousPosition == self.PlayerInfo.Position):
                    if(gameMap.getTileAt(self.PlayerInfo.Position+self.previousDirection).TileContent == TileContent.Wall):
                        return create_attack_action(self.previousDirection)
                    if(gameMap.getTileAt(self.PlayerInfo.Position+self.previousDirection).TileContent == TileContent.Resource):
                        return create_collect_action(self.previousDirection)
                    if(self.previousDirection.y != 1):
                        return create_move_action(Point(0,1))
                    else :
                        return create_move_action(Point(1, 0))
                direction = path[1] - self.PlayerInfo.Position
            else:
                if self.PlayerInfo.Position == self.PlayerInfo.HouseLocation:
                    self.goingToHouse = False 
                    return self.upgrade()
                else:
                    directionOOS = self.PlayerInfo.HouseLocation
                    pos = Point(min(max(directionOOS.x, gameMap.xMin+1), gameMap.xMax-1), min(max(directionOOS.y, gameMap.yMin+1), gameMap.yMax-1))
                    path = shortestPath(translate(gameMap.tiles), self.PlayerInfo.Position, pos)
                    print(self.PlayerInfo.Position)
                    direction = path[1] - self.PlayerInfo.Position
            self.previousPosition = self.PlayerInfo.Position
            self.previousDirection = direction
        if abs(direction.x) < abs(direction.y):
            if(direction.y != 0):
                dirY = int(direction.y/abs(direction.y))
            else:
                dirY = 0
            if gameMap.getTileAt(self.PlayerInfo.Position + Point(0, dirY)).TileContent == TileContent.Wall or gameMap.getTileAt(self.PlayerInfo.Position + Point(0, dirY)).TileContent == TileContent.Resource:
                return create_attack_action(Point(0, dirY))
            return create_move_action(Point(0, dirY))
        else:
            if(direction.x !=0):
                dirX = int(direction.x/abs(direction.x))
            else:
                dirX = 0
            if gameMap.getTileAt(self.PlayerInfo.Position + Point(dirX, 0)).TileContent == TileContent.Wall or gameMap.getTileAt(self.PlayerInfo.Position + Point(dirX, 0)).TileContent == TileContent.Resource:
                return create_attack_action(Point(dirX, 0))
            return create_move_action(Point(dirX, 0))
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(-1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    # def getPath(self, playerPosition, destination, gameMap):
    #     direction = destination - playerPosition
    #     if abs(direction.x) < abs(direction.y):
    #         newPosition = playerPosition+(Point(0, int(direction.y/abs(direction.y))))
    #     else:
    #         newPosition = playerPosition+(Point(int(direction.x/abs(direction.x)), 0))
    #     if gameMap.getTileAt(newPosition).TileContent == TileContent.Empty:
    #         return newPosition
    #     return None

    def upgrade(self):
        if(self.PlayerInfo.getUpgradeLevel(UpgradeType.CollectingSpeed)< self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity) ):
            return create_upgrade_action(UpgradeType.CollectingSpeed)
        elif(self.PlayerInfo.getUpgradeLevel(UpgradeType.AttackPower) < self.PlayerInfo.getUpgradeLevel(UpgradeType.CarryingCapacity)):
            return create_upgrade_action(UpgradeType.AttackPower)
        else:
            return create_upgrade_action(UpgradeType.CarryingCapacity)
