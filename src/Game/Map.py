import pytmx as pytmx
import pyscroll as pyscroll
import pygame
from OPTIONS import *

class Map:
    def __init__(self,tmx_map_path:str, screen) -> None:
        self.tmx_data = pytmx.util_pygame.load_pygame(tmx_map_path)
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, screen.get_size(), clamp_camera = True)
        self.map_layer.zoom = 2.5 * (SCREENINFO.RES[0]/720)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer)
    
    def get_spawn_point(self):
        return self.tmx_data.get_object_by_name("spawn_player")

    def get_collision_object(self):
        collision_objects = []
        for obj in self.tmx_data.objects:
            if obj.name == "collision":
                collision_objects.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        return collision_objects
    
    def get_obstacle_area(self):
        obstacle_area = []
        for obj in self.tmx_data.objects:
            if obj.name == "spawn_obstacle":
                obstacle_area.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height-10))
        return obstacle_area
    
    def get_spawns_obj(self):
        spawns_obj = []
        for obj in self.tmx_data.objects:
            if obj.name == "spawn_obj":
                spawns_obj.append([obj.x, obj.y])
        return spawns_obj
            
    def get_respawn_obj(self):
        respawn_obj = []
        for obj in self.tmx_data.objects:
            if obj.name == "respawn":
                respawn_obj.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        return respawn_obj
    
    def add_in_group(self, obj):
        self.group.add(obj)

    def remove_in_group(self, obj):
        self.group.remove(obj)