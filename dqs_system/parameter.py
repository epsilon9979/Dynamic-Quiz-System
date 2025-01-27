
def get_para(goal):
    para={'NEWS_APIKEY':'f', # use your own key
        'BASE_URL':'https://newsapi.org/v2/everything',
        'MEDIA':'cnn',
        
        'info_api':['/Performance/EyPolicy',
                        '/ExecutiveYuan/NewsEy',
                        '/Performance/EyResolution'],
        
        'ChatGPT_API':'', # use your own key
        'ChatGPT_model':"gpt-4o-mini",
        'resources_amount':[10, 10, 10, 3],
        'expire_days':92,
        'update_days':1,
        'DATABASE_NAME':'questions_warehouse',
        'TABLE_NAME':['Keelung', 'New_Taipei', 'Taipei', 'Taoyuan', 'Hsinchu', 'Miaoli', 'Taichung',
                        'Changhua', 'Nantou', 'Yunlin', 'Chiayi', 'Tainan', 'Kaohsiung', 'Pingtung',
                        'Taitung', 'Hualien', 'Yilan', 'Lienchiang', 'Kinmen', 'Penghu', 'international'],
        'county_list':['基隆市','新北市','臺北市','桃園市','新竹','苗栗縣','臺中市','彰化縣','南投縣','雲林縣',
                        '嘉義縣','臺南市','高雄市','屏東縣','臺東縣','花蓮縣','宜蘭縣','連江縣','金門縣','澎湖縣','international']
        }
    
    return para[goal]