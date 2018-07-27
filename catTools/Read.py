import json

def readFile(path):
    with open(path) as notebookFile:
        s = notebookFile.read()   #notebook本身为json格式的字典
        return turnToJson(s)

def turnToJson(jsons):
    notebookDic = json.loads(jsons)  #此处通过json将文件转换为python字典的格式
    cells = notebookDic['cells']     #取出字典‘cells’对应的值
    del notebookDic['cells']         #保留字典中metadata
    return cells, notebookDic        #返回字典的值和metadata
