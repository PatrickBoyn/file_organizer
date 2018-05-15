import os

dirs = ['exe', 'pdf', 'html', 'zip', 'crdownload', 'dll', 'ppt', 'jpg']

path = r'C:\Users\dakil\Desktop\PreDelete'

os.chdir(path)

for i in dirs:
    os.mkdir(i)
