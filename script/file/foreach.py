# _*_ coding: utf-8 _*_
import os
import time
import uuid
import hashlib


def md5_me(key):
    md5 = hashlib.md5()
    md5.update(str(key).encode('utf-8'))
    value = md5.hexdigest()
    return value


def get_uuid():
    res = str(uuid.uuid4())
    UUID = ''.join(res.split('-'))
    return UUID


# 把时间戳转换成格式化
def timestamp_to_str(timestamp=None, format='%Y-%m-%d %H:%M:%S'):
    if timestamp:
        time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
        result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
        return result
    else:
        return time.strptime(format)


def main():
    dirPath = r'E:\QQ\850781645\FileRecv\留学图片\留学图片'
    file_list = os.listdir(dirPath)
    # print(file_list)
    i = 0
    for dir_name_item in file_list:
        path_item = dirPath + os.sep + dir_name_item
        print(path_item, ' ----- ', dir_name_item)
        # 进入子目录
        # for root, dirs, files in os.walk(path_item):
        #     for item in files:
        #         print(item)
        i += 1
        u = get_uuid() + "-" + str(i)
        with open(path_item, 'rb') as f, \
                open(r'images/{}.jpg'.format(u), 'wb') as fw, \
                open('res.txt', 'a+', encoding='utf-8') as ffw:
            t = f.read()
            fw.write(t)
            ffw.write(f"//xxx.xxx.cn/image/peony/merchant/202008/{u}.jpg" + '\n')


if __name__ == '__main__':
    main()
