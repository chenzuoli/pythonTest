# --coding--=utf=8

if __name__ == '__main__':
    print('----使用 python自带的open() 写文件-----')
    path = r'writeMe.txt'
    f = open(path, mode='w')
    f.write("我是Python写入的。")
    f.close()
