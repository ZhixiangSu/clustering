import pandas as pd
import numpy as np
import sys
import KD_Tree
from queue import Queue
def DBSCAN(input_file,output_file,radius,number):
    data=pd.read_excel(input_file)
    label=1
    vis=np.zeros(len(data))
    def dist(a,b):
        dist1=0
        for i in range(len(a)):
            dist1+=np.square((a[i]-b[i]))
        dist1=np.sqrt(dist1)
        return dist1

    def DFS(center,label):
        q=Queue()
        for i in range(len(data)):
            if vis[i]==0and(dist(data.values[i],center)<r):
                vis[i]=label
                q.put(i)
        if(q.qsize()>=num):
            while(q.empty()==False):
                DFS(data.values[q.get()],label)
    for i in range(len(data)):
        if vis[i]==0:
            vis[i]=label
            DFS(data.values[i],label)
            label+=1
    vis=pd.DataFrame(vis)
    writer=pd.ExcelWriter(output_file)
    vis.to_excel(writer,sheet_name="Label")
    writer.close()
def DBSCAN_KD(input_file,output_file,radius,number):
    data=pd.read_excel(input_file)
    Root=KD_Tree.divide(data,0)
    def DFS(center):
        q=Queue()
        for i in range(number):
            point=KD_Tree.search(Root,center.level,center.data)
            point.vis=center.vis
            if(KD_Tree.dist(point.data,center.data)<radius):
                q.put(point)
        if(q.qsize()==number):
            while q.empty()==False:
                DFS(q.get())
    def S_Tree(root):
        label = 1
        if root.left!=None:
            S_Tree(root.left)
        if root.right!=None:
            S_Tree(root.right)
        if(root.vis==0):
            root.vis=label
            DFS(root)
            label=label+1
    S_Tree(Root)
    def P_Tree(root):
        if root.left!=None:
            P_Tree(root.left)
        if root.right!=None:
            P_Tree(root.right)
        print(root.data)
        print(root.vis)
        P_Tree(root)
if __name__ == '__main__':
    input_file = "input.xls"
    output_file = "output.xls"
    r = 0.3
    num = 20
    sys.setrecursionlimit(100000)#增大递归深度
    DBSCAN(input_file,output_file,r,num)

