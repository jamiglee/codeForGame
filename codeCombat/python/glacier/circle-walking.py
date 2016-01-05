# http://cn.codecombat.com/play/level/circle-walking
# Mirror your partner's movement around the center X mark.
# Vectors can be thought of as an x, y position
# Vectors 可以反映两个位置之间的距离和方向。

# use Vector.subtract(vector1, vector2) to find the direction and distance from vector2 to vector1
# 使用 Vector.add(vector1, vector2) 找到你从 vector1 到 vector2 的位置

# 在 X 点的中心创建一个新的 Vector
center = Vector(40, 34)

# 一个单位的位置实际是一个 Vector！
partner = self.findByType("peasant")[0]

loop:
    # 首先，您要找到伙伴位置到 X 中心的 Vector（距离和方向）。
    # vector = Vector(partner.pos.x, partner.pos.y)
    diff = Vector.subtract(center, partner.pos)
    # Second, find the position your hero should moveTo starting from center, and following vector.
    moveToPos = Vector.add(center, diff)

    # Third, move to the moveToPos position.
    self.move(moveToPos)
    pass
