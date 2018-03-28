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
            people_group.append(People.People(m))
            cabin_map.locate_people(people_group[m-1],i,j)
cabin_map.people_group=people_group

m=0
seats=[]
for i in range(2,60,2):
    for j in range(0,8,1):
        if j==3 or j==4:
            continue
        else:
            m=m+1
            seats.append(Monument.Monument(m))
            cabin_map.locate_monument(seats[m-1],i,j)
cabin_map.monuments=seats

exit_doors=[]
exit_doors.append(Monument.ExitDoor(1))
cabin_map.locate_exit(exit_doors[0],0,0)
exit_doors.append(Monument.ExitDoor(2))
cabin_map.locate_exit(exit_doors[1],0,7)
cabin_map.exits=exit_doors

#intinal ends

#Loop


print('hello')

