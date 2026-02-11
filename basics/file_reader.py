user_file_path = input("Enter your file absolute path: ")

f = open(user_file_path,"r")

for line in f.readlines():
    print(line.strip())

f.close()