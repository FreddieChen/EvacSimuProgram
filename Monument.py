#-*- coding: utf-8 -*-

class Monument(object):
    num_of_monument=0
    
    def __init__(self,my_id,type,location,size_x,size_y,height,direction,passable):
        self.my_id=my_id
        self.type=type
        self.location=location
        self.size_x=size_x
        self.size_y=size_y
        self.height=height
        self.direction=direction
        self.passable=passable

class ExitDoor(object):

    def __init__(self,my_id,door_type,location,direction):
    