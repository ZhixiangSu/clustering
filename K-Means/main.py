import pandas as pd
import numpy as np
def K_Means(input_file,output_file,initial_center):
    data=pd.read_excel(input_file)      #读取文件
    center=pd.DataFrame(initial_center)     #初始化中心格式
    label=np.zeros(len(data),np.int)        #标签初始化为0
    num=np.zeros(len(center),np.int)        #每个类中点的个数初始化为0
    def dist(x,y):      #定义距离函数（欧几里得距离）
        d=0
        for i in range(len(x)):
            d+=np.square(x[i]-y[i])
        d=np.sqrt(d)
        return d
    for t in range(30):        #循环次数
        label=np.zeros_like(label,np.int)
        num = np.zeros_like(num,np.int)
        for i in range(len(data)):      #遍历样本中的点
            min=1000000000
            for j in range(len(center)):        #寻找最近中心
                dist1=dist(data.values[i],center.values[j])
                if dist1<min:
                    min=dist1
                    label[i]=j          #修改点的标签
            num[label[i]]+=1            #修改类中的点数
        initial_center=np.zeros_like(initial_center,np.float)       #清空初始中心（方便计算新的中心）
        center=pd.DataFrame(initial_center)
        for i in range(len(data)):          #根据类中的点计算新的中心
            for j in range(len(center.values[0])):
                center.values[label[i]][j]+=data.values[i][j]/num[label[i]]
    writer = pd.ExcelWriter(output_file)        #制作Excel表格
    center.to_excel(writer,sheet_name="centers")        #第一个sheet
    pd.DataFrame(label).to_excel(writer,sheet_name="labels")        #第二个sheet
    writer.close()
'''
筛选寻找合适的中心点
def set_initial_center(initial_values,initial_center,line,value):
    if line<len(initial_values):
        for i in range(len(initial_values[line])):
            value1=value+[initial_values[line][i]]
            set_initial_center(initial_values,initial_center,line+1,value1)
    else:initial_center.append(value)
'''
if __name__ == '__main__':
    input_file = "../input.xls"
    output_file = "output.xls"
    initial_center=[[0.3, 0.2, 0.2, 0.2, 0, 0.8],       #初始中心
                     [0.3, 0.2, 0.2, 1.5, 0, 0.8],
                     [0.3, 0.2, 0.2, 1.5, 1.2, 1.4],
                     [2.2, 0.2, 0.2, 0.2, 0, 0.8],
                     [2.2, 0.2, 0.2, 0.2, 1.2, 1],
                     [2.2, 0.2, 0.2, 0.2, 1.2, 1.4]]
#    initial_center=[]
#    set_initial_center(initial_values,initial_center,0,[])
    K_Means(input_file, output_file, initial_center)