from helper import *

class Bot:
    def __init__(self):
        self.goingToHouse = False


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
        res = list()
        for x in range(gameMap.xMax):
            for y in range(gameMap.yMax):
                if gameMap.getTileAt(Point(x,y)) == TileContent.Resource:
                    res.append(Point(x,y))
                elif gameMap.getTileAt(Point(x,y)) == TileContent.House:
                    house = Point(x,y)
        if not self.goingToHouse:
            res.sort(key=lambda p: Point.Distance(p, self.PlayerInfo.Position))
            print(res)
            if not len(res):
                self.goingToHouse=True
                return
            index = 0
            pathFound = False
            while not pathFound:
                closestRes = res[index]
                playerPosition = self.PlayerInfo.Position
                while Point.Distance(playerPosition, closestRes) > 1:
                    print(playerPosition)
                    position = self.getPath(playerPosition, closestRes, gameMap)
                    if not position:
                        index+=1
                        break
                    else:
                        playerPosition = position
                if Point.Distance(playerPosition, closestRes) <= 1:
                    pathFound = True


            direction = closestRes - self.PlayerInfo.Position
            print(closestRes)
            print(self.PlayerInfo.Position)
            print(direction)
            print(self.PlayerInfo.TotalResources)
            if Point.Distance(self.PlayerInfo.Position, closestRes) <= 1:
                if(direction.x !=0):
                    dirX = int(direction.x/abs(direction.x))
                else:
                    dirX = 0
                if(direction.y != 0):
                    dirY = int(direction.y/abs(direction.y))
                else:
                    dirY = 0
                if(dirX ==0 and dirY==0):
                    self.goingToHouse = True
                return create_collect_action(Point(dirX, dirY))
            if self.PlayerInfo.TotalResources >= self.PlayerInfo.CarryingCapacity:
                self.goingToHouse = True
        else:
            direction = self.PlayerInfo.HouseLocation - self.PlayerInfo.Position
            if direction.x ==0 and direction.y == 0 :
                self.goingToHouse = False 
                return create_upgrade_action(UpgradeType.CollectingSpeed)
        if abs(direction.x) < abs(direction.y):
            if(direction.y != 0):
                dirY = int(direction.y/abs(direction.y))
            else:
                dirY = 0
            return create_move_action(Point(0, dirY))
        else:
            if(direction.x !=0):
                dirX = int(direction.x/abs(direction.x))
            else:
                dirX = 0
            return create_move_action(Point(dirX, 0))
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(-1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def getPath(self, playerPosition, destination, gameMap):
        direction = destination - playerPosition
        if abs(direction.x) < abs(direction.y):
            newPosition = playerPosition+(Point(0, int(direction.y/abs(direction.y))))
        else:
            newPosition = playerPosition+(Point(int(direction.x/abs(direction.x)), 0))
        if gameMap.getTileAt(newPosition) == TileContent.Empty:
            return newPosition
        return None

    def findClosestResource(self, gameMap):
        pass

