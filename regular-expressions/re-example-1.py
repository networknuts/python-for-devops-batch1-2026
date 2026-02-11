import re

f = open("/home/aryan/python-8am-wd/python-for-devops/email-list.txt","r")
data = f.read()
f.close()

result = re.search(r"[b,r]obb[i,y]",data)
print(result)