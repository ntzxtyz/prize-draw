import os

out = open("people.stage3.json",'w')
out.write("[")
def turn(name):
    return name.encode("unicode-escape").decode()
def change(fil):
    print(fil)
    name = fil[9:fil.find('.')]
    out.write('''{"avatar":"photos/''' + fil + '''","studentId":"''' + fil[0:9] + '''","studentName":"''' + turn(name) + '''"},''')
    return
fs = os.listdir("./photos")
for f in fs:
    if not os.path.isdir(f):
        change(f)
