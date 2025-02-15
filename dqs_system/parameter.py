
def get_para(goal):
    para={'NEWS_APIKEY':'', # use your own key
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
        'TABLE_NAME':['Keelung', 'New_Taipei', 'Taipei', 'Taipei', 'Taoyuan', 'Hsinchu', 'Miaoli', 'Taichung', 'Taichung',
                        'Changhua', 'Nantou', 'Yunlin', 'Chiayi', 'Tainan', 'Tainan', 'Kaohsiung', 'Pingtung',
                        'Taitung', 'Taitung', 'Hualien', 'Yilan', 'Lienchiang', 'Kinmen', 'Penghu', 'international', 'energy'],
        'county_list':['基隆','新北','臺北','台北','桃園','新竹','苗栗','臺中', '台中','彰化','南投','雲林',
                        '嘉義','臺南', '台南', '高雄','屏東','臺東','台東','花蓮','宜蘭','連江','金門','澎湖','international', 'energy']
        }
    
    return para[goal]