# -*- coding: utf-8 -*-


class Map(object):
    # 地图类
    def __init__(self,cabin_length,cabin_width,cell_length):
        self.length = cabin_length  # 地图长度
        self.width = cabin_width    # 地图宽度
        self.cell_length = cell_length       # 网格边长
        self.cell_x_num=int(cabin_length/cell_length)
        self.cell_y_num=int(cabin_width/cell_length
        self.cells = [[Cell(i, j, cell_length) for j in range(self.cell_y_num)]
                      for i in range(self.cells_x_num)]
        self.time=0
        # 网格矩阵
    def next_time(self,delt_t):
        self.calculate_distance()

    def calculate_distance(self,exit_doors):
        for exit_door in exit_doors:
            exit_door.location.nearest_exit=exit_door
            exit_door.location.distance_to_nearest_exit=0






class Cell(object):
    # 网格类
    def __init__(self, i, j, cell_length):
        self.my_id = (i, j)              # 网格编号
        self.location = ((i+0.5)*cell_length, (j+0.5)*cell_length)  # 网格中心位置x,y
        self.monument = None          # 网格内的物体
        self.people = None            # 网格内的人
        self.next_people=None         # 下一时间步长的人
        self.nearest_exit=None        # 最近的出口
        self.distance_to_nearest_exit=0   # 到最近出口的距离
        self.x_th=i                    # x轴第几个
        self.y_th=j                    # y轴第几个


