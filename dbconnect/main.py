import pandas as pd
import mysql.connector

db = mysql.connector.connect(user = 'pasindu', database = 'eleccare',password ='1234')
cursor = db.cursor()

query = "select date,time,power from elec_usage"
cursor.execute(query)

myallData = cursor.fetchall()

all_datetime = []
# all_date = []
# all_time = []
all_power = []
for  date ,time,power in myallData:
    dt = str(date)+" "+str(time)
    all_datetime.append(dt)
    # all_date.append(date)
    # all_time.append(time)
    all_power.append(power)

#we need to store this data to CSV
#dic = {'Date' : all_date ,'Time':all_time, 'AEP_MW':all_energy}

dic = {'Datetime' : all_datetime , 'AEP_MW':all_power}
df = pd.DataFrame (dic)
df_csv = df.to_csv('./PZEM_AEP_hourly.csv')
