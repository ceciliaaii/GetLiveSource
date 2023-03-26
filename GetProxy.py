# import requests
# from lxml import etree
#
# # https://free.kuaidaili.com/free/inha/2/
# def send_re(self,page):
# for i in range(1,90):
#     print("=============正在抓取第{}页===========".format(page))
#     url = '# https://free.kuaidaili.com/free/inha/{}/'.format()
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
#     }
#     # print(url)
#     request = requests.get(url=url,headers=headers)
#     content = request.content.decode('utf-8')
#     print(content)
import os

# 文件夹的路径
scr = 'D:\pythonProject1'
# 获取文件夹下的txt的文件名
fs = os.listdir(scr)
print(fs)
for fz in fs:
    # txt文件路径
    src_folder = scr + "\\" + fz
    images = src_folder
    print(images)
    # 以只读模式读取文件

    # 路径
    path = images
    file = open(path, "r")
    lines = []
    for i in file:
        lines.append(i)  # 逐行将文本存入列表lines中

    file.close()

    # 创建一个新的列表，用于存储改变之后的内容
    new = []

    for line in lines:  # 逐行遍历

        # 选择需要添加的内容 line[0:] --->"E:\DATASET\VOC2028_hat\JPEGImages" + "\\" + line[0:]
        new.append("E:\DATASET\VOC2028_hat\JPEGImages" + "\\" + line[0:])

    file_write_obj = open(path, 'w')

    for var in new:
        file_write_obj.writelines(var)

    file_write_obj.close()