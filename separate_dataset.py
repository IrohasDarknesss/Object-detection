import os
import shutil
import glob
import random

path_list = glob.glob('./dataset/train/*jpg')

def separate_dataset(path, sep):
    file_list = path
    list_len = len(file_list)
    n = int(list_len*sep)

    z = random.sample(file_list, list_len)
    train_list = z[:n]
    test_list = z[n:]

    val_file = './dataset/val/'

    print (len(file_list))
    print (len(train_list))
    print (len(test_list))

    for test_path in test_list:
        print(test_path)
        shutil.move(test_path, val_file)
    return [train_list,test_list]

if __name__ == '__main__':
    separate_dataset(path_list, 0.7)