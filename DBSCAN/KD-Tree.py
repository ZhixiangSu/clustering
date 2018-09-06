import pandas as pd
import numpy as np

class Node:
    def __init__(self,data,level):
        self.data=data
        self.level=level
    def add_left(self,node):
        self.left=node
    def add_right(self,node):
        self.right=node
input=pd.DataFrame([[2,3],[5,4],[4,7],[7,2],[8,1],[9,6]],columns=['x1','x2'])
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
root=divide(input,0)
print(root)