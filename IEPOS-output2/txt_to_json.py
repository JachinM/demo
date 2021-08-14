import os
import json
with open( "used_conf.txt" ) as f:
        lines = f.readlines()
dataList = lines[1:]
dataL = [sentence.strip('==============\n') for sentence in dataList]
data = [sentences.strip('--------------') for sentences in dataL]
for a in data:
    if a == '':
        data.remove(a)
f = [sentence2.replace(": "," = ") for sentence2 in data]
result_list=[]
for i in f:
    result={}
    list = i.split(" = ")
    result["configuration"]=list[0]
    result["value"] = list[1]
    result_list.append(result)
with open("IEPOS_output2_used_conf_to_json.txt","w") as file1:
    jsonfile = json.dumps(result_list)
    file1.write(jsonfile)