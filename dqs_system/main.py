from Step import Pipeline
from pipeline.cnn_resources_api import get_resource_int
from pipeline.resources_api import get_resource
from pipeline.data_update import filter
from pipeline.chatgpt_api import manufacture
from pipeline.upload_question import insertquestions
from pipeline.database import record

def main(): 
    inputs = {} 
    
    for round in range(4):
        steps = [
            [get_resource(), get_resource(), get_resource(), get_resource_int()][round],
            filter(),
            manufacture(),
            insertquestions(),
        ] 
        
        print('round ', round)
        database = record()
        a = Pipeline(steps)
        a.run(database, round)
    
    
if __name__ == '__main__':
    main()