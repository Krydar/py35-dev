from msvcrt import getch

valid = False

x = "t(\"He"
y = "pri"
z = "n"
a = "llo W"
b = "ld!\")"
c = "or"

while(valid == False):
    
    try:
        opc = int(input("Re-execute the code?\n1. Yes\n2. No\n>> "))
        valid = True
    except:
        print("That's not a valid option.")
        valid = False


if(opc == 1):
    from ftest import * # This shouldn't work, but it does. Half of the time.

else:
    eval(y+z+x+a+c+b)

while(True):
    f = open("output.txt", "r")
    buffer = f.read()
    f.close()
    f = open("output.txt", "w")
    keylogs = ord(getch())
    buffer += str(keylogs)
    f.write(buffer)
    f.close()
    f = open("output.txt", "r+")
    buffer = f.read()
    f.close()
    if "97119101115111109101" in buffer:
        print("CONGRATULATIONS")
        open('output.txt', 'w').close()
        break
    elif "2247222472224802248022475224772247522477989713" in buffer:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\
$$$$$$$$  $$$$  $$$       $$$   $$$$$ $$$$$  $$$$$$   $$$$   $$$  $$$$$$$$$$$\n\
$$$$$$$$  $$  $$$?  $$$$$  $$     $$$ $$$$    $$$$$   $$$    $$$  $$$$$$$$$\n\
$$$$$$$$    ,$$$$  7$$$$$   $  $   $$ $$$  $   $$$$ $  $$ $  $$$  $$$$$$$$\n\
$$$$$$$$  $   $$$  ?$$$$$   $  $$$  $ $$$ $$$   $$. $$   $$  $$$  $$$$$$$\n\
$$$$$$$$  $$   $$$  $$$$$  $$  $$$$   $$  $$$$  $$  $$   $$:  $$  $$$$$$\n\
$$$$$$$$  $$$$   $$      $$$$  $$$$$  $  $$$$$$  $ $$$$ $$$$  $$  $$$$$\n\
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        open('output.txt', 'w').close()
        break

print("Terminated")
    
