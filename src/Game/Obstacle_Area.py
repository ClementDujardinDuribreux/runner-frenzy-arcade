import random
from Game.Obstacle import Obstacle

class Obstacle_Area:

    def __init__(self, map, y_area, height):
        self.nb_obstacle = 3
        self.map = map
        self.y_area = y_area
        self.height = height
        self.sprite_list = ['sprites/_rock1.png',
                            'sprites/_rock2.png',
                            'sprites/_fence.png',
                            'sprites/_arbre.png',
                            'sprites/_bush.png']
        self.obstacle_list = []
        self.generate_obstacles()

    def get_obstacle_list(self):
        rect_obj_list = []
        for obj in self.obstacle_list:
            rect_obj_list.append(obj.feet)
        return rect_obj_list
    
    def generate_spawn_point(self):
        list_position = []
        list_spawn_point = [i for i in range(350 + 25, 610-16, 40)]
        for _ in range(0, len(self.obstacle_list)):
            random_x_spawn = random.randint(0, len(list_spawn_point)-1)
            list_position.append(list_spawn_point[random_x_spawn])
            del list_spawn_point[random_x_spawn]
        return list_position       
        
    def generate_obstacles(self):
        
        for _ in range(self.nb_obstacle):
            random_sprite = random.randint(0,len(self.sprite_list) - 1)
            if self.sprite_list[random_sprite] == 'sprites/_arbre.png':
                new_obstacle = Obstacle(self.sprite_list[random_sprite], 32, 48)
            elif self.sprite_list[random_sprite] == 'sprites/_fence.png':
                new_obstacle = Obstacle(self.sprite_list[random_sprite], 40, 30)
            elif self.sprite_list[random_sprite] == 'sprites/_bush.png':
                new_obstacle = Obstacle(self.sprite_list[random_sprite], 22, 17)
            else : new_obstacle = Obstacle(self.sprite_list[random_sprite])
            self.map.add_in_group(new_obstacle)
            self.obstacle_list.append(new_obstacle)
            list_position = self.generate_spawn_point()

        for i in range(0, len(self.obstacle_list)):
            if self.obstacle_list[i].sprite == 'sprites/_arbre.png':
                self.obstacle_list[i].set_entity_spawn(list_position[i], self.y_area-16)
            elif self.obstacle_list[i].sprite == 'sprites/_bush.png':
                self.obstacle_list[i].set_entity_spawn(list_position[i], self.y_area+15)
            else : self.obstacle_list[i].set_entity_spawn(list_position[i], self.y_area)
    
    def delete_obstacles(self):
        for obstacle in self.obstacle_list:
            self.map.remove_in_group(obstacle)
            self.obstacle_list = []
            del obstacle