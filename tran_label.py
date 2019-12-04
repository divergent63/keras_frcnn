import os
path="/home/zz-guo/keras_frcnn/kitti/training/label_2/"
pathi="/home/zz-guo/keras_frcnn/kitti/training/image_2/"
path_new="/home/zz-guo/keras_frcnn/kitti/labels_new.txt"
files = os.listdir(path)
file_new = open(path_new,'w')
for file in files:
    f = open(os.path.join(path,file))
    lines = f.readlines()
    for line in lines:
        line = line.split()
        if line[0] != 'DontCare':
            file_new.writelines(os.path.join(pathi,file.split('.')[0]+'.png')+','+line[4]+','+line[5]+','+line[6]+','+line[7]+','+line[0]+'\n')
