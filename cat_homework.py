import json
import sys

# handle argument exceptions
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')


# accept argument list
notebook_path_lst = sys.argv[1:]

target_notebook = {}
cells_lst = []

# read notebook path list
for path in notebook_path_lst:
    with open(path) as notebook:
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cells = notebook_json['cells']
        cells_lst += cells

target_notebook['cells'] = cells_lst

#完成cells提取

matedata = open(sys.argv[1])
matedata_str = matedata.read()
matedata_json = json.loads(matedata_str)
del matedata_json['cells']
# 提取只包含metadata的字典

target_notebook.update(matedata_json)
target_str = json.dumps(target_notebook)
target = open('target_notebook.ipynb', 'w')
target.write(target_str)


#异常处理作业，如果没有参数输入，会怎么样？