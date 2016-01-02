# Defend your towers in this replayable challenge level!
# Step on an X if you have 20 gold to build a soldier.
# http://cn.codecombat.com/play/level/sarven-siege
#

def getPosition(x, y):
    return {"x":x, "y":y}

towerY = [51, 78, 22]

loop:
    for y in towerY:
        flag = self.findFlag()
        if flag:
            self.move(flag.pos)
            self.pickUpFlag(flag)
        else:
            coins = self.findItems()
            coin = self.findNearest(coins)
            distance = 9999
            for i in coins:
                if i.value >= 2 and self.distanceTo(i) < distance:
                    distance = self.distanceTo(i)
                    coin = i
            if
            self.move(coin.pos)

            if self.gold >= 20:
                self.move(getPosition(84, y))
                # self.moveXY(84, y)