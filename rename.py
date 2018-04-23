#coding=utf-8
import os
import cv2

path = "frames"
count=0
imgs = os.listdir(path)

for img in imgs:

    Olddir = os.path.join(path, img);  # 原来的文件路径

    if os.path.isdir(Olddir):  # 如果是文件夹则跳过

        continue;
    img_name=str(path) +"//"+ str(img)
    ii = cv2.imread(img_name)
    ii=cv2.resize(ii,(500,500))
    cv2.imwrite(img_name,ii)
    filename = os.path.splitext(img)[0];  # 文件名



    Newdir = os.path.join(path, str(0+count) + ".jpg");  # 新的文件路径

    os.rename(Olddir, Newdir);  # 重命名
    print(count)
    count += 1;
'''
path = "/home/zkc/zkc/ocr/CCDL-master/tools/ssd-lab/test_all"
count=0
imgs = os.listdir(path)

for img in imgs:

    Olddir = os.path.join(path, img);  # 原来的文件路径

    if os.path.isdir(Olddir):  # 如果是文件夹则跳过

        continue;



    Newdir = os.path.join(path, str(count) + ".bmp");  # 新的文件路径

    os.rename(Olddir, Newdir);  # 重命名
    print count
    count += 1;
'''