import re

f = open("/home/aryan/python-8am-wd/python-for-devops/email-list.txt","r")
data = f.read()
f.close()

# Example 1
result = re.search(r"chr[a-z][a-z]",data)
print(result)

# Example 2
result = re.search(r"chr[a-z]{2}", data)
print(result)

# Example 3
result = re.search(r"tho[a-z]+", data)
print(result)