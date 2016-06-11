from msvcrt import getch

while(True):
    f = ord(getch())
    print(f)
    if(f == 13):
        break
