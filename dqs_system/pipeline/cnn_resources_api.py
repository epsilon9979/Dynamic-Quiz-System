import requests
from bs4 import BeautifulSoup
from parameter import get_para
from datetime import datetime
from Step import STEPS

class get_resource_int(STEPS):
    
    def process(self, data, database):
        print("in resource")
        round = data.pop()
        API_KEY = get_para('NEWS_APIKEY')
        BASE_URL = get_para('BASE_URL') 
        media = get_para('MEDIA')
        num =  get_para('resources_amount')[round] 
        
        def scrapt(link):
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')  # 解析 HTML 內容
                paragraphs = soup.find_all('p') # 這裡可以根據需要提取具體的內容。 例如，提取所有的段落文字
                material = ''
                for paragraph in paragraphs:
                    a = paragraph.get_text()
                    material = material + a
                return material
            else:
                print("無法訪問網頁，狀態碼:", response.status_code)
        
        params = {
            'q': 'world',  # 查詢關鍵字
            'sources': media,  # 指定來源為 CNN
            'apiKey': API_KEY,  # API 金鑰
            'language': 'en',  # 語言設置
            'sortBy': 'publishedAt',  # 按發佈時間排序(relevancy, popularity, publishedAt)
            'pageSize': num  # 返回的新聞數量
        }
        
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            disaster_news = []
            for news in data['articles']:
                content = news['description']
                link = news['url']
                rawdate = news['publishedAt'] # 2024-09-27T10:50:34Z
                article = scrapt(link)
                date = datetime.strptime(rawdate, "%Y-%m-%dT%H:%M:%SZ")
                material = {}
                material['內容'] = article
                material['上版日期'] = date
                material['county'] = ["international"]
                material['標題'] = news['title']
                material['來源網址'] = link
                disaster_news.append(material)
                continue
                    
        print(disaster_news)
        return disaster_news
        
        