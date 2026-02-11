import re

ip_raw_file = input("Enter log file containing IPV4 addresses: ")
ip_finished_file = input("Enter file to redirect found IPV4s in: ")

f = open(ip_raw_file,"r")
data = f.read()
f.close()

print("File read successfully!")
print("="*10)
#result = re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", data)
result = re.findall(r"\d+\.\d+\.\d+\.\d+", data) #character classes
# \d = character class
print(result)
print("="*10)

f = open(ip_finished_file,"w")
for ip in result:
    f.write(ip+"\n")
f.close()

print(f"IPs successfully extracted in file: {ip_finished_file}")