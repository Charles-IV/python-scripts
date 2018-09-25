from time import sleep

def add(x,y):
    z = x + y  # perform calculation
    print(z)  # output result
    sleep(0.2)  # HOLD! STOP! WAIT, to not kill my computer
    add(y, z)  # perform next calculation

add(0, 1)
