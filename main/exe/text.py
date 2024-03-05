# -*- coding: utf-8 -*-
import os
import zipfile

# python 实现 压缩当前目录下package 文件夹的文件为text.zip 文件


# 设置包含要压缩文件的目录名和目标zip文件名
directory_to_zip = 'dist'
zip_filename = 'text.zip'

# 使用绝对路径可以避免潜在的问题
abs_dir_to_zip = os.path.abspath(directory_to_zip)

# 创建一个ZipFile对象，使用'w'模式以写入新的zip文件
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # os.walk可以遍历文件夹中的所有文件和子文件夹
    for dirname, subdirs, files in os.walk(directory_to_zip):
        # 将文件夹名称添加到zip文件中
        zipf.write(dirname)
        for filename in files:
            # 计算文件的路径
            absname = os.path.abspath(os.path.join(dirname, filename))
            # 计算保存到zip文件中的文件名
            arcname = absname[len(abs_dir_to_zip) + 1:]
            print('zipping %s as %s' % (absname, arcname))
            # 将文件写入zip文件中，使用之前计算的文件名
            zipf.write(absname, arcname)

print(f'{directory_to_zip} has been zipped into {zip_filename}')

