import json
from . import Read

class Notebook:
    def __init__(self,path = None):
        if path is not None:
            self.cells ,self.metaData = Read.readFile(path)

    def __add__(self,anther):
        cells = self.cells + anther.cells
        notebook = Notebook()
        Notebook.cells = cells
        notebook.metaData = self.metaData  #
        return notebook

    def jsons(self):
        dct = {'cells':self.cells}
        dct.update(self.metaData)
        return json.dumps(dct, indent = 4)
    
        
