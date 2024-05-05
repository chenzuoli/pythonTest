# --coding--=utf-8


if __name__ == '__main__':
    print('----使用 python自带的open() 读取文件-----')
    path = r'readMe.txt'
    f = open(path, mode='r')
    print(f.readlines())

    f.close()
