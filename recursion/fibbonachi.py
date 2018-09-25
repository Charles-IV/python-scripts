from time import sleep

def add(x=0,y=1):
    z = x + y
    print(z)
    sleep(0.2)
    add(y, z)

add()
