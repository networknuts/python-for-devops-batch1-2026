import os
import time
import humanize

def walking(parent_path):
    print(f"Starting directory walk in {parent_path}")
    children = os.listdir(parent_path)
    for child in children:
        child_path = os.path.join(parent_path,child) #/home/aryan/.ssh /home/aryan - parent, .ssh - child
        if os.path.isfile(child_path):
            child_info = os.stat(child_path)
            print(f"File: {child_path}")
            print(f"Size: {humanize.naturalsize(child_info.st_size)}")
            print(f"Access Time: {time.ctime(child_info.st_atime)}")
            print(f"Creation Time: {time.ctime(child_info.st_ctime)}")
            print("-------")
        elif os.path.isdir(child_path):
            walking(child_path)


parent_path = input("Enter main directory: ")
walking(parent_path)