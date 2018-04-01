# -*- coding: utf-8 -*-

class People(object):
    num_of_people=0
    
    def __init__(self,my_id):
        self.type='People'
        self.my_id=my_id
        self.location = None
        self.max_velocity=1
        self.velocity=None
        self.chosen_exit=None
        self.direction=None
        self.next_location=None
        self.memory=[]
        People.num_of_people=People.num_of_people+1