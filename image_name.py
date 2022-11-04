import glob
import os

path = glob.glob('./data/*.jpg')

n = 1
for name in path:
    # print(name)
    os.rename(name, './data/liella_' + str(n) + '.jpg')
    n += 1