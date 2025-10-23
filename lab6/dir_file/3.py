import os
p = "a.txt"
if os.path.exists(p):
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("not exists")