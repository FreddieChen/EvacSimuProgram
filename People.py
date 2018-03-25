# -*- coding: utf-8 -*-

class People(object):
    num_of_people=0
    
    def __init__(self,my_id,age,weight,height,gender,character):
        self.my_id=my_id
        self.age=age
        self.weight=weight
        self.height=height
        self.gender=gender
        self.character=character
        self.max_velocity=None
        self.body_state=None
        self.velocity=None
        self.location=None
        self.chosen_exit=None
        self.direction=None
        self.next_location=None
        self.memory=[]
        People.num_of_people=num_of_people+1
    
    def ChangeBodyState(self):
    
    def ChooseExit(self):
    
    def ChooseDirection(self):  
    
    def OpenDoor(self,Door):
    
    
class Attendant(People):
    def __init__(self,my_id,age,weight,height,gender,character):
        People.__init__(self,my_id,age,weight,height,gender,character)
    
    def GuidePeople(self):
    
    def SpeedUpPeople(self):