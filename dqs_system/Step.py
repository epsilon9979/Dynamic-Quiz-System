from abc import ABC
from abc import abstractmethod

class STEPS(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def process(self, data, database):
        pass
 
class STEPexception(Exception):
    pass
  
###################################################################################################
class Pipeline:
    def __init__(self, which_step):
        self.steps = which_step
        
    def run(self, database, round):
        data = []
        data.append(round)
        for step in self.steps:
            try:
                data = step.process(data, database)  #執行每一個步驟的程式功能
            except STEPexception as e:
                print('exception happened', e)
                break