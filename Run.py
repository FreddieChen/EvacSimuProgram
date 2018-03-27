# -*- coding: utf-8 -*-

import Map
import Monument
import People

#initial
cabin_map=Map.Map(30,4,0.5)

people_group=[]
m=0
for i in range(1,59,2):
    for j in range(0,8,1):
        if j==3 or j==4:
            continue
        else:
            m=m+1
            people_group.append(People.People(m,cabin_map.cells[i][j]))
            cabin_map.cells[i][j].people=people_group[m-1]
m=0
seats=[]
for i in range(2,60,2):
    for j in range(0,8,1):
        if j==3 or j==4:
            continue
        else:
            m=m+1
            seats.append(Monument.Monument(m,'seat',cabin_map.cells[i][j]))
            cabin_map.cells[i][j].monument=seats[m-1]

exit_doors=[]
exit_doors.append(Monument.ExitDoor(1,'exit',cabin_map.cells[0][0]))
exit_doors.append(Monument.ExitDoor(2,'exit',cabin_map.cells[0][7]))
#intinal ends

#Loop


print('hello')

