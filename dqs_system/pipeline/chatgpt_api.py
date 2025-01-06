from openai import OpenAI
from Step import STEPS
from parameter import get_para


class manufacture(STEPS):
    
    def process(self, data, database):
        print("in manufacture")
        API_key = get_para('ChatGPT_API')
        client = OpenAI(api_key = API_key)
        # openai.api_key = API_key
        prompt1 = "妳現在是宣傳公關，請整理出四大重點"
        prompt2 = "根據這四項重點，幫我出一題選擇題，「目的是讓使用者知道發生什麼事」。並附上「答案解釋」。依照以下格式：### 選擇題\n\n**問題：** ......？ \n\nA) ......  \nB) ......  \nC) ......  \nD) ......  \n\n**正確答案： ......\n\n### 答案解釋：\n....."
        
        def ChatGPT(content):
            user_message = content
            chat_log.append({"role":"user", "content":user_message})
            response = client.chat.completions.create(
                model = "gpt-4",
                messages = chat_log
                )
            response2 = response.choices[0].message.content
            answer = response2.strip("\n").strip()
            return answer
        
        series = []
        #print(data)#########################################################################
        for news in data:
            questions = {}
            chat_log = []
            content = news['內容']
            time = news['上版日期']
            order1 = content + prompt1
            response1 = ChatGPT(order1)

            order2 = response1 + prompt2
            response2 = ChatGPT(order2)
            chat_log = []
            questions['rawquestion'] = response2
            questions['time'] = time
            questions['county'] = news['county']
            series.append(questions)
        
        print(series)
        return series        
                    
                    
        