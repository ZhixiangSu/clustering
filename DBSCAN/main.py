import pandas as pd
import numpy as np
import sys
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
    '''
    q=Queue()
    for j in range(len(data)):
        if vis[j]==0:
            vis[j]=label
            q.put(j)
        while(q.empty()==False):
            center=data.values[q.get()]
            for i in range(len(data)):
                if vis[i] == 0 and (dist(data.values[i], center) < r):
                    vis[i] = label
                    q.put(i)
        label+=1
    '''
    vis=pd.DataFrame(vis)
    writer=pd.ExcelWriter(output_file)
    vis.to_excel(writer,sheet_name="Label")
    writer.close()
if __name__ == '__main__':
    input_file = "../input.xls"
    output_file = "output2.xls"
    r = 0.3
    num = 20
    sys.setrecursionlimit(100000)#增大递归深度
    DBSCAN(input_file,output_file,r,num)
