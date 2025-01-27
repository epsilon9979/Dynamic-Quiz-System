from Step import STEPS
from parameter import get_para
import random

class insertquestions(STEPS):
    
    def process(self, data, database):
        print("in insertquestions")
        cursor, cnx = database.setting()
        
        def id_generator(existed_id):
            valid_num = [i for i in range(0, 100) if i not in existed_id]
            return random.choice(valid_num)
        
        for batch in data:
            material_1 = batch['rawquestion']
            time = batch['time']
            material_2 = material_1.replace('**','')
            material_3 = material_2.replace('###','')
            material_4 = material_3.replace('\n\n','\n')
            components = material_4.split('\n')
            del components[0]   
            try:
                components.remove(' 答案解釋：')
            except:
                pass
            components.append(time)
            
            for county in batch['county']:
                table_name = county
                existed_id = database.fetch(cursor, cnx, table_name, 'id', None)
                id = id_generator(existed_id)
                components.insert(0, id)
                achievement = tuple(components)
                database.append(cursor, cnx, achievement, table_name)
                del components[0]
            print(achievement)