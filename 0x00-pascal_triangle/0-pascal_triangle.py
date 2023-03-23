#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        list = []
    else:
        list = [1]
        for a in range(n):
            print(list)
            newlist=[]
            newlist.append(list[0])
            for a in range(len(list)-1):
                newlist.append(list[a]+list[a+1])
            newlist.append(list[-1])
            list=newlist
