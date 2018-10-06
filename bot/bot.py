from helper import *

class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo
        self.goingToHouse = False

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        res = list()
        for x in range(gameMap.xMax):
            for y in range(gameMap.yMax):
                if gameMap.getTileAt(Point(x,y)) == 4:
                    res.append(Point(x,y))
                elif gameMap.getTileAt(Point(x,y)) == 2:
                    house = Point(x,y)
        if not self.goingToHouse:
            minDist = float('inf')
            closestRes = Point()
            for resource in res:
                dist = Point.Distance(resource, self.PlayerInfo.Position)
                if dist < minDist:
                    minDist = dist
                    closestRes = resource
            direction = closestRes - self.PlayerInfo.Position
            if Point.Distance(self.PlayerInfo.Position, closestRes):
                return create_collect_action(direction)
            if self.PlayerInfo.TotalResources >= self.PlayerInfo.CarryingCapacity:
                self.goingToHouse = True
        else:
            direction = house - self.PlayerInfo.Position
        if direction.x < direction.y:
                return create_move_action(Point(0, direction.y))
            else:
                return create_move_action(Point(direction.x, 0))
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
