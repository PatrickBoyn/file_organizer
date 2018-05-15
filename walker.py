import os
import shutil
import re


# The starting location.
walking = r'C:\Users\dakil\Downloads'
# The destination to move to.
changing = r'C:\Users\dakil\Desktop\PreDelete'

# The various file types will be sorted into these folders. 
subdir = ['\dll', '\exe', '\html', '\jpg', '\pdf', '\ppt', '\zip','\crdownload', '\Delete']

# The appended version of changing. 
result = []

# Appends subdir to changing.
for a in subdir:
    result.append(changing + a)
print(result[0])

print()

# Move to the desired location.
def mover(num):
    shutil.move(full_path, result[num])

# If it is of file type x, move it to location y. 
for folders, sub, file in os.walk(walking):
    for i in file:
        full_path = os.path.join(folders, i)
        print(full_path)
        if full_path.endswith('dll') == True:
            mover(0)
        elif full_path.endswith('exe') == True:
            mover(1)
        elif full_path.endswith('html') == True:
            mover(2)
        elif full_path.endswith('jpg') == True:
            mover(3)
        elif full_path.endswith('pdf') == True:
            mover(4)
        elif full_path.endswith('ppt') == True:
            mover(5)
        elif full_path.endswith('zip') || fullpath.endswith('rar')== True:
            mover(6)
        elif full_path.endswith('crdownload') == True:
            mover(7)
        else:
            mover(8)

