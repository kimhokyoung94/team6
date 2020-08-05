import pandas as pd
import numpy as np
import pymysql
data = pd.read_csv("./data.csv",encoding='CP949')
dataf = pd.DataFrame(data)
print(dataf.head())

db = pymysql.connect(host='localhost', 
                        port=3306, 
                        user='root', 
                        passwd='1234', 
                        db='myflaskapp')
cursor  = db.cursor()
cursor.connection.encoders[np.int64] = lambda value, encoders: int(value)
sql = '''
INSERT INTO `myflaskapp`.`monitoring_data` (`Lux`, `Temp`, `Humid`, `Date`, `Time`, `user_id`)
 VALUES (%d, %d,%d,%s,%s,%d);
'''
for i in range(len(dataf)):
    a=tuple(dataf.loc[i])
    cursor.execute(sql,a[1:])
    db.commit()


