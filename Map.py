# -*- coding: utf-8 -*-


class Map(object):
    # 地图类
    def __init__(self, aircraft, cell_length):
        self.length = aircraft.cabin_length  # 地图长度
        self.width = aircraft.cabin_width    # 地图宽度
        self.cell_length = cell_length       # 网格边长
        self.cells = [[Cell(i, j, cell_length) for j in range(int(aircraft.cabin_width/cell_length))]
                      for i in range(int(aircraft.cabin_length/cell_length))]
        # 网格矩阵


class Cell(object):
    # 网格类
    def __init__(self, i, j, cell_length):
        self.my_id = (i, j)              # 网格编号
        self.location = [(i+0.5)*cell_length, (j+0.5)*cell_length]  # 网格中心位置x,y
        self.monument = None          # 网格内的物体
        self.people = None            # 网格内的人
        self.environment = None       # 网格内的环境
        self.passable = None          # 网格可通行性


class Aircraft(object):
    # 飞机类
    def __init__(self, cabin_length, cabin_width):
        self.cabin_length = cabin_length
        self.cabin_width = cabin_width

