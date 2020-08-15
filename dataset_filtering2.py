# *_*coding: utf-8 *_*
# author --blair--

"""
本程序对数据集label中含有白色背景的数据对剔除
"""
import os
import cv2
import time
import shutil

# 开始时间
t_start = time.time()
# 读取和存储路径
sats_path = 'G:/llx_dataset/sat/'
labels_path = 'G:/llx_dataset/label/'
sats_save_path = 'G:/llx_dataset2/sat/'
labels_save_path = 'G:/llx_dataset2/label/'
# 一条边测试点数
one_side_points = 16
# 将四个角不为白色的图像复制到新的路径
labels = [f for f in os.listdir(labels_path) if f.endswith(".tif")]
total = len(labels)
# print(labels)
for num, label in enumerate(labels):
    label_img = cv2.imread(labels_path + label, 0)
    # print(label_img.shape)
    height, width = label_img.shape
    Top_side_has_white = False  # 假设图像上面一条边不含有白色
    # 上面一条边
    for j in range(0, width, width // one_side_points):  # 宽
        if label_img[0, j] != 255:
            continue
        else:
            Top_side_has_white = True
            print(label, ' top has white')
            break
    if not Top_side_has_white:  # 如果上面一条边不含有白色
        Right_side_has_white = False  # 假设图像右面一条边不含有白色
        # 右边一条边
        for i in range(0, height, height // one_side_points):  # 高
            if label_img[i, width - 1] != 255:
                continue
            else:
                Right_side_has_white = True
                print(label, ' right has white')
                break
        if not Right_side_has_white:  # 如果右边一条边不含有白色
            Bottom_side_has_white = False  # 假设图像下边一条边不含有白色
            # 下面一条边
            for j in range(width - 1, -1, - width // one_side_points):  # 宽
                if label_img[height - 1, j] != 255:
                    continue
                else:
                    Bottom_side_has_white = True
                    print(label, ' bottom has white')
                    break
            if not Bottom_side_has_white:  # 如果下面一条边不含有白色
                Left_side_has_white = False  # 假设图像左边一条边不含有白色
                # 左边一条边
                for i in range(height - 1, -1, - height // one_side_points):  # 高
                    if label_img[i, 0] != 255:
                        continue
                    else:
                        Left_side_has_white = True
                        print(label, ' left has white')
                        break
                if not Left_side_has_white:  # 如果左边一条边不含有白色，那就每条边都不含白色
                    shutil.copy(labels_path + label, labels_save_path)
                    # sat和label同名
                    shutil.copy(sats_path + label, sats_save_path)
    if (num + 1) % 1000 == 0:  # 每1000个输出一次
        t_used = int(time.time() - t_start)
        print('处理进度：{}/{},已耗时{}s'.format(num + 1, total, t_used))

# 结束时间
t_end = time.time()
print('处理完毕,耗时:{}秒'.format(round((t_end - t_start), 4)))
