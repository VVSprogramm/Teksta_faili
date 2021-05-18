f = open("teksts.txt")  #atveram failu
saturs = f.read()       #nolasām faila saturu
f.close()               #aizveram failu
print(saturs)           #izvadām faila saturu