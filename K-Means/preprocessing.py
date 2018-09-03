import pandas as pd
import numpy as np
raw_file="raw_data.xls"
data_file="data.xls"
raw_data=pd.read_excel(raw_file,sheet_name="航空公司客户数据")
duration=raw_data["LOAD_TIME"]-raw_data["FIRST_FLIGHT_DATE"]
duration.columns=["DURATION"]
total_income=raw_data["EXPENSE_SUM_YR_1"]+raw_data["EXPENSE_SUM_YR_2"]
data=pd.concat([raw_data["FFP_DATE"],duration,raw_data["FLIGHT_COUNT"],total_income,raw_data["SEG_KM_SUM"],raw_data["LAST_FLIGHT_DATE"],raw_data["avg_discount"]],axis=1)
writer=pd.ExcelWriter(data_file)
data.to_excel(writer)
writer.close()