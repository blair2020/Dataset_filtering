# *_*coding: utf-8 *_*
# author --blair--

"""
本程序对数据集label中含有白色背景的数据对剔除
缺点：只检测了四个角
改进参看dataset_filtering2.py
"""

import os
import cv2
import time
import shutil

# 开始时间
t_start = time.time()
# 读取和存储路径
sats_path = 'G:/cliped_sat_label/sat/'
labels_path = 'G:/cliped_sat_label/label/'
sats_save_path = 'G:/llx_dataset/sat/'
labels_save_path = 'G:/llx_dataset/label/'

# 将四个角不为白色的图像复制到新的路径
labels = [f for f in os.listdir(labels_path) if f.endswith(".tif")]
total = len(labels)
# print(labels)
for num, label in enumerate(labels):
    label_img = cv2.imread(labels_path + label, 0)
    # print(label_img.shape)
    height, width = label_img.shape
    if label_img[0, 0] != 255 and label_img[0, width - 1] != 255 and label_img[height - 1, 0] != 255 and label_img[
        height - 1, width - 1] != 255:
        shutil.copy(labels_path + label, labels_save_path)
        # sat和label同名
        shutil.copy(sats_path + label, sats_save_path)
    t_used = int(time.time() - t_start)
    print('{}已处理,处理进度：{}/{},已耗时{}s'.format(label, num + 1, total, t_used))

# 结束时间
t_end = time.time()
print('处理完毕,耗时:{}秒'.format(round((t_end - t_start), 4)))