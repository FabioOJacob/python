import winsound
b=winsound.Beep
b(1000,1000)
b(500,500)

import time
s=time.sleep
for i in range(1,5):
    for j in range(1,5):
        b(100*j*i,50)
        s(0.01)
s(0.01)