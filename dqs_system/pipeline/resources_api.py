import requests
from parameter import get_para
from datetime import datetime
from Step import STEPS

class get_resource(STEPS):
    
    def process(self, data, database):
        print("in resource")
        round = data.pop()
        info_api = get_para('info_api')[round]
        num = str(get_para('resources_amount')[round]) 
        api_url = 'https://opendata.ey.gov.tw/api' + info_api + '?MaxSize=' + num + '&IsRemoveHtmlTag=true'

        # 設定 headers，指定接受 JSON 格式
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            rawdata = response.json()
        else:
            print(f"請求失敗，狀態碼：{response.status_code}")
        
        #判斷內容是否為縣市相關，並做標記
        county_list = get_para('county_list')
        table_name = get_para('TABLE_NAME')
        rawdata_2 = []
        for news in rawdata:
            content = news['內容']
            county = []
            for i in county_list:
                if i in content:
                    county.append( table_name[ county_list.index(i) ] )
            if len(county)>0:
                news['county'] = county
                rawdata_2.append(news)
        
        for news in rawdata_2:
            date = news['上版日期'] 
            y,m,d = map(int,date.split('/'))
            newdate = datetime(y,m,d)
            news['上版日期'] = newdate
        print(rawdata_2)    
        return rawdata_2
    