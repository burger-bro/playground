import os
import sys

dir_path = "/Users/fredericshaw/Documents/grad/calc18exe"
cnt = 0
for filename in os.listdir(dir_path):
    if filename.endswith(".png"):
        cnt += 1
        filenames = filename.split(" ")
        filenames[0] = filenames[0].replace("_", filenames[0][-2:])
        filenames[0] = filenames[0][:-2]
        new_filename = " ".join(filenames)
        print(new_filename)
        os.system(f"cp '{dir_path}/{filename}' '{dir_path}rename/{new_filename}'")
print("cnt", cnt)
