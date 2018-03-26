#-*- coding: utf-8 -*-

class Monument(object):
    num_of_monument=0
    
    def __init__(self,my_id,type,location):
        self.my_id=my_id          # 座椅的编号
        self.type=type            #  ='seat'
        self.location=location    # 座椅的位置
        self.add_in_distance=5    # 由于座椅增加的距离，翻阅座椅的时间5秒

class ExitDoor(object):

    def __init__(self,my_id,type,location):
        self.my_id=my_id          # 出口的编号
        self.type=type            #  ='Exit'
        self.location=location    # 位置
    