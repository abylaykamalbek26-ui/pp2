import os
file = r"C:\Users\Abylay\projects\pp2\lab6\dir_file\a.txt" 

if os.path.exists(file):
    if os.access(file, os.R_OK):
        os.remove(file)  
        print("file removed")
    
else:
    print("file didnt exists")