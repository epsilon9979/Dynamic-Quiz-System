import datetime
from  datetime import datetime, timedelta
from Step import STEPS
from parameter import get_para

class filter(STEPS):
    
    def process(self, data, database):
        print("in filter")
        expire_num = int( get_para('expire_days') )
        update_days = int( get_para('update_days') )
        table_name = get_para('TABLE_NAME')
    
        def days_ago(date): #date須為datetime的日期形式
            a = datetime.now()
            b = date
            c = b-a
            c_seconds = abs(int(c.total_seconds())/86400)
            return c_seconds
        
        def expire_days(dayss):
            a = datetime.now()
            b = timedelta(days=dayss)
            expire_date = a - b
            return expire_date
        
        #篩選rawdata_2
        material = []  
        for news in data:
            time = news['上版日期']
            days = days_ago(time)
            if days < update_days:
                material.append(news)
        
        #刪除過期題目
        cursor, cnx = database.setting()
        for stuff in material:
            for county in table_name:
                if county in stuff['county']:
                    database.create_table(cursor, county)
                    
        existed_tables = database.show_tables(cursor)
        for table in existed_tables:
            expire_date = expire_days(expire_num)
            criteria = f"date < '{expire_date}'"
            database.delete(cursor, cnx, table, criteria)
            if len(database.fetch(cursor, cnx, table, 'id', None)) == 0:
                database.drop_table(cursor, table)  
                print(f"dropping table {table}") 
        return material 