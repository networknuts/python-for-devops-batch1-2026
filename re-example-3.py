import re

f = open("/home/aryan/python-8am-wd/python-for-devops/email-list.txt","r")
data = f.read()
f.close()

#result = re.search(r"[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+",data)
result = re.search(r"\w+@\w+\.\w+",data)
print(result)