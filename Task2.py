import subprocess
from glob import glob  # list all the files in alist

All_Images = glob('/home/salma/Desktop/X2/*.jpg')
c = 0

for i in All_Images:
    data = "exiftool {0} > /home/salma/Desktop/Output/output{1}.txt".format(
        i, c)
    result2 = subprocess.check_output(
        data, shell=True, text=True)
    print(result2)
    c += 1
