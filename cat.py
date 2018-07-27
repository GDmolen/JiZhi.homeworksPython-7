import json
import sys
from catTools import Cated

argv = sys.argv[1:]
if len(argv) < 2:
    raise Exception('参数数量必须大于2')
notebookLst = []

for Path in argv:
    if '.ipynb' not in Path:
        Path += '.ipynb'
    notebookLst.append(Cated.Notebook(Path))  #针对每一哥路径生成一个notebook对象

targetNotebook = notebookLst[0]
for i in notebookLst[1:]:
    targetNotebook += i  #把多个notebook的实例对象合并成一个

with open('targetNotebook.ipnyb', 'w') as targetFile:
    targetFile.write(targetNotebook.jsons())  #最后添加的类方法