import pandas as pd
import numpy as np
input_file="input.xlsx"
output_file="output.xlsx"
data=pd.read_excel(input_file)
initial_center=[
    [1,1],
    [10,10],
    [10,1]
]
center=pd.DataFrame(initial_center)
label=np.zeros(len(data),np.int)
num=np.zeros(len(center),np.int)
def dist(x,y):
    d=0
    for i in range(len(x)):
        d+=np.square(x[i]-y[i])
    d=np.sqrt(d)
    return d
for t in range(100):
    label=np.zeros_like(label,np.int)
    num = np.zeros_like(num,np.int)
    for i in range(len(data)):
        min=1000000000
        for j in range(len(center)):
            dist1=dist(data.values[i],center.values[j])
            if dist1<min:
                min=dist1
                label[i]=j
        num[label[i]]+=1
    initial_center=np.zeros_like(initial_center,np.float)
    center=pd.DataFrame(initial_center)
    for i in range(len(data)):
        for j in range(len(center.values[0])):
            center.values[label[i]][j]+=data.values[i][j]/num[label[i]]
writer = pd.ExcelWriter(output_file)
center.to_excel(writer)
writer.close()