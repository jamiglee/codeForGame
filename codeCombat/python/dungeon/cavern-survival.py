# 生存时间比敌人的英雄长！

def heroAttack():
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    if enemy:
        while enemy.health > 0:
            if self.distanceTo(enemy) > 7 and self.isReady("jump"):
                self.jumpTo(enemy.pos)

            if self.isReady("bash"):
                self.bash(enemy)
            else:
                self.attack(enemy)

def summonFriends():
    if self.gold > self.costOf("griffin-rider"):
        self.summon("griffin-rider")
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")

def commandFriends():
    friends = self.findFriends()
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    for i in friends:
        if enemy:
            self.command(i, "attack", enemy)
        else:
            self.command(i, "defend", self.pos)

loop:
    # 制定自己的战略。有创意!
    summonFriends()
    commandFriends()
    heroAttack()
