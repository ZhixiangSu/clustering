import pandas as pd
import numpy as np

class Node:
    def __init__(self,data,level):
        self.data=data
        self.level=level
        self.left=None
        self.right=None
        self.vis=int(0)
    def add_left(self,node):
        self.left=node
    def add_right(self,node):
        self.right=node
input=pd.DataFrame([[2,3],[5,4],[4,7],[7,2],[8,1],[9,6]],columns=['x1','x2'])
def dist(x,y):
    d=0
    for i in range(len(x)):
       d+=np.square(x[i]-y[i])
    d=np.sqrt(d)
    return d
def divide(data,level):
    node=Node(data.values[0],level)
    left_data=[]
    right_data=[]
    for i in range(1,len(data)):
        if data.values[i][level%len(data.values[0])]<data.values[0][level%len(data.values[0])]:
            left_data.append(data.values[i])
        else:
            right_data.append(data.values[i])
    left_data=pd.DataFrame(left_data)
    right_data=pd.DataFrame(right_data)
    if len((left_data))>0:
        node.add_left(divide(left_data,level+1))
    if len((right_data)) > 0:
        node.add_right(divide(right_data,level+1))
    return node
def search(root,level,center):
    if(root.vis!=0):
        return None
    if center[level%len(root.data)]<root.data[level%len(root.data)]:
        if root.left!=None:
            point=search(root.left,level+1,center)
        else:
            point=root
    else:
        if root.right!=None:
            point=search(root.right,level+1,center)
        else:
            point=root
    radius=dist(point.data,center)
    if(radius>np.abs(center[level%len(root.data)]-root.data[level%len(root.data)])):
        point2=None
        if point==root.left:
            if root.right!=None:
                point2=search(root.right,level+1,center)
            else:
                point2 = root
        else:
            if root.left!=None:
                point2=search(root.left,level+1,center)
            else:
                point2 = root
        if(dist(point2.data,center)<radius):
            point=point2
    if(dist(root.data,center)<dist(point.data,center)):
        point=root
    return point