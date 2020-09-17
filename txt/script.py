import json
filename = "A.txt"
dict1 = {}
fields =['name', 'type', 'desc', 'orign']
with open(filename, encoding="utf8") as fh:
    for line in fh: 
         
        # reads each line and trims of extra the spaces  
        # and gives only the valid words 
        command, description = line.strip().split("*")
  
        dict1[command] = description.strip() 
  
# creating json file 
# the JSON file is named as test1 
out_file = open("test1.json", "w") 
json.dump(dict1, out_file, indent = 4, sort_keys = False) 
out_file.close()  