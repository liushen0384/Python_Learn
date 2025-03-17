"""

"""

import json  # 调用json模块

# 列表转换为json格式数据
date = [{"name": "liushen", "age": "lushuai"}, {"name": "liushen", "age": "lushuai"}, {"name": "liushen", "age": "lushuai"}]
json_date = json.dumps(date, ensure_ascii = False) # ensure_ascii = False表示不适用ascii码转换，为了使中文正常显示
print(type(json_date), json_date)

# 字典转换为json格式数据
dict1 = {"name": "liushen", "age": "lushuai"}
json_date = json.dumps(dict1)
print(type(json_date), json_date)

# json格式转换回列表
json_date = '[{"name": "liushen", "age": "lushuai"}, {"name": "liushen", "age": "lushuai"}, {"name": "liushen", "age": "lushuai"}]'
date = json.loads(json_date)
print(type(date), date)

# json转换为字典
json_date = '{"name": "liushen", "age": "lushuai"}'
date = json.loads(json_date)
print(type(date), date)

