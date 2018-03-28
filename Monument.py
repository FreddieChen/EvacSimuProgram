#-*- coding: utf-8 -*-

class Monument(object):
    num_of_monument=0
    
    def __init__(self,my_id):
        self.my_id=my_id          # 座椅的编号
        self.type='seat'            #  ='seat'
        self.location=None    # 座椅的位置
        self.add_in_distance=5    # 由于座椅增加的距离，翻阅座椅的时间5秒
        Monument.num_of_monument=Monument.num_of_monument+1

class ExitDoor(object):
    num_of_exit_door=0

    def __init__(self,my_id):
        self.my_id=my_id          # 出口的编号
        self.type='exit'            #  ='Exit'
        self.location=None    # 位置
        ExitDoor.num_of_exit_door=ExitDoor.num_of_exit_door+1
    