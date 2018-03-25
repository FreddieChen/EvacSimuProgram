# -*- coding: utf-8 -*-

import Map

b737 = Map.Aircraft(100, 5)
b737_map = Map.Map(b737, 1)
print(b737_map.cells[3][2].x)
