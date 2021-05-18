f = open("teksts.txt")  #atveram failu
saturs = f.read()       #nolasām faila saturu
f.close()               #aizveram failu
print(saturs)           #izvadām faila saturu


z = open("tagad_taisam.txt", "w")  #faila izveidošana
z.write("Tev sanāca arī šis!")
z.close()