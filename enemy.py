class Enemy():
    def __init__(self,enemy_height, enemy_width,health,velocity,x_pos,y_pos,moving_right,moving_left,idle,attacking,
                 direction_facing):
        self.enemy_height = enemy_height
        self.enemy_width = enemy_width
        self.health = health
        self.velocity = velocity
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.moving_right = moving_right
        self.moving_left = moving_left
        self.idle = idle
        self.attacking = attacking
        self.direction_facing = direction_facing


