import pandas as pd
import numpy as np
import math
raw_file="raw_data.xls"
data_file="data.xls"
input_file="input.xls"
def preprocessing(raw_file,data_file,input_file):
    #数据提取
    input_columns_name=['DURATION','FLIGHT_COUNT','TOTAL_INCOME', 'SEG_KM_SUM', 'LAST_FLIGHT', 'avg_discount']
    raw_data=pd.read_excel(raw_file,sheet_name="航空公司客户数据")
    duration=raw_data["LOAD_TIME"]-raw_data["FIRST_FLIGHT_DATE"]
    duration.rename("DURATION")
    total_income=raw_data["EXPENSE_SUM_YR_1"]+raw_data["EXPENSE_SUM_YR_2"]
    last_time_to_load_time=raw_data["LOAD_TIME"]-raw_data["LAST_FLIGHT_DATE"]
    input_data=pd.concat([duration,raw_data["FLIGHT_COUNT"],total_income,raw_data["SEG_KM_SUM"],last_time_to_load_time,raw_data["avg_discount"]],axis=1)
    data=pd.concat([raw_data["FFP_DATE"],raw_data["LOAD_TIME"],raw_data["FLIGHT_COUNT"],raw_data["EXPENSE_SUM_YR_1"],raw_data["EXPENSE_SUM_YR_2"],raw_data["LAST_FLIGHT_DATE"]],axis=1)
    input_data.columns=input_columns_name
    #数据格式化
    input_data["DURATION"]=input_data["DURATION"]/np.timedelta64(1,'D')
    input_data['FLIGHT_COUNT']=input_data['FLIGHT_COUNT'].astype('float64')
    input_data['TOTAL_INCOME']=input_data['TOTAL_INCOME'].astype('float64')
    input_data[ 'SEG_KM_SUM'] =input_data[ 'SEG_KM_SUM'].astype('float64')
    input_data["LAST_FLIGHT"] = input_data["LAST_FLIGHT"] / np.timedelta64(1, 'D')
    input_data['avg_discount'] =input_data['avg_discount'].astype('float64')
    #统一数量级
    input_data["DURATION"] = input_data["DURATION"]/input_data["DURATION"].mean()
    input_data['FLIGHT_COUNT'] = input_data['FLIGHT_COUNT'] / input_data['FLIGHT_COUNT'].mean()
    input_data['TOTAL_INCOME'] = input_data['TOTAL_INCOME'] / input_data['TOTAL_INCOME'].mean()
    input_data['SEG_KM_SUM'] = input_data['SEG_KM_SUM'] / input_data['SEG_KM_SUM'].mean()
    input_data["LAST_FLIGHT"] = input_data["LAST_FLIGHT"] / input_data["LAST_FLIGHT"].mean()
    input_data['avg_discount'] = input_data['avg_discount'] / input_data['avg_discount'].mean()
    #删除缺失数据
    invalid=[]
    for i in range(len(input_data)):
        for j in range(len(input_columns_name)):
            if math.isnan(input_data.values[i][j]):
                invalid.append(i)
                break
    input_data.drop(invalid,inplace=True,axis=0)
    #数据保存
    data_writer=pd.ExcelWriter(data_file)
    data.to_excel(data_writer)
    data_writer.close()
    input_writer=pd.ExcelWriter(input_file)
    input_data.to_excel(input_writer)
    input_writer.close()
if __name__ == '__main__':
    raw_file = "raw_data.xls"
    data_file = "data.xls"              #相关数据
    input_file = "input.xls"            #有效输入数据
    preprocessing(raw_file,data_file,input_file)