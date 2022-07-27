import re
import os
def find_pic_name(log_path):  # 找到文件中的执行图片名称
    '''
    从日志中找到执行图片名
    params log_name 日志文件名
    return pic_info,当文件不存在或者结果不存在时返回
    {'depth_image_size': '图片不存在', 'color_image_info': '图片不存在'}
    '''
    file_path = log_path  # 文件地址拼接
    pic_time = []
    try:
        with open(file_path, 'r') as reader:  # 打开文件
            log_lines = reader.readlines()

            for line_index, char in enumerate(log_lines):
                if '彩色图尺寸' in char:
                    pic_line = log_lines[line_index]
                    # 通过re将pose匹配出来，形成 7个一组的列表
                    pic_line = re.match(r'''(.*)depth image尺寸:(.*)彩色图尺寸:(.*)''', pic_line)
                    # print(pic_line.group(2))
                    # print(pic_line.group(3))
                    # print(pic_line.group(1)[0:8])
                    pic_time.append(pic_line.group(1)[0:8].replace(':',''))

            return pic_time

    except:
        print("文件不存在或者文件中没有对应的内容")
        return {'depth_image_size': '图片不存在', 'color_image_info': '图片不存在'}


def find_all_pic_time(dir_path):
    file_list = []
    file_time = []
    for root, dirs, files in os.walk(dir_path):
        # print(files)
        file_list = files

    for file_name in file_list:
        file_time.append(file_name[-14:-8])

    return file_time


pic_time = find_pic_name(r"F:\数据保存测试数据\chongdianlogds\2022-08-03.log")
print(pic_time)

aa = find_all_pic_time(r"F:\数据保存测试数据\datajiqiren\2022-08-03\TAM05217A3020653-color")
# print(aa)
bb = find_all_pic_time(r"F:\数据保存测试数据\datachongdiankou\2022-08-03\TAM05217A3020653-color")
# print(bb)

cc = aa+bb
cc.sort()
print(cc)

pic_time = find_pic_name(r"F:\数据保存测试数据\chongdianlogds\2022-08-04.log")
print(pic_time)

aa = find_all_pic_time(r"F:\数据保存测试数据\datajiqiren\2022-08-04\TAM05217A3020653-color")
# print(aa)
bb = find_all_pic_time(r"F:\数据保存测试数据\datachongdiankou\2022-08-04\TAM05217A3020653-color")
# print(bb)

cc = aa+bb
cc.sort()
print(cc)

pic_time = find_pic_name(r"F:\数据保存测试数据\chongdianlogds\2022-08-05.log")
print(pic_time)

aa = find_all_pic_time(r"F:\数据保存测试数据\datajiqiren\2022-08-05\TAM05217A3020653-color")
# print(aa)
bb = find_all_pic_time(r"F:\数据保存测试数据\datachongdiankou\2022-08-05\TAM05217A3020653-color")
# print(bb)

cc = aa+bb
cc.sort()
print(cc)
