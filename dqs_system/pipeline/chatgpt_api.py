from openai import OpenAI
from Step import STEPS
from parameter import get_para


class manufacture(STEPS):
    
    def process(self, data, database):
        print("in manufacture")
        API_key = get_para('ChatGPT_API')
        ChatGPT_model = get_para('ChatGPT_model')
        county_list = get_para('county_list')
        table_name = get_para('TABLE_NAME')
        client = OpenAI(api_key = API_key)
        # openai.api_key = API_key
        
        def ChatGPT(content):
            user_message = content
            chat_log.append({"role":"user", "content":user_message})
            response = client.chat.completions.create(
                model = ChatGPT_model,
                messages = chat_log
                )
            response2 = response.choices[0].message.content
            answer = response2.strip("\n").strip()
            return answer
        
        series = []
        #print(data)#########################################################################
        for news in data:
            for city in news['county']:
                county = county_list[ table_name.index(city) ]
                prompt1 = f"你現在是宣傳公關，請整理出「四大重點」以及「跟{county}的關聯」"
                prompt2 = f"根據這五個要點，幫我出一題選擇題，「目的是讓使用者知道發生什麼事」且「要跟{county}有關」。依照以下格式：### 選擇題\n\n**問題：** ......？ \n\nA) ......  \nB) ......  \nC) ......  \nD) ......  \n\n**正確答案： ......"
                prompt3 = "接著給我答案解釋，90字以內，並務必確保文句中沒有「選項」和「A、B、C、D」等字眼"
                prompt4 = "把'答案解釋'加在上述已完成之選擇題的最後，依照以下格式：### 選擇題\n\n**問題：** ......？ \n\nA) ......  \nB) ......  \nC) ......  \nD) ......  \n\n**正確答案： ......\n\n### 答案解釋：\n....."
                questions = {}
                chat_log = []
                content = news['內容']
                order1 = content + prompt1
                response1 = ChatGPT(order1)
                order2 = response1 + prompt2
                response2 = ChatGPT(order2)
                order3 = response2 + prompt3
                response3 = ChatGPT(order3)
                order4 = response3 + prompt4
                response4 = ChatGPT(order4)

                questions['rawquestion'] = response4
                questions['county'] = city
                questions['time'] = news['上版日期']
                questions['title'] = news['標題']
                questions['url'] = news['來源網址']
                series.append(questions)
        
        print(series)
        return series        
                    
                    
        