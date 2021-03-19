def main():
    print('======数据管理======')
    print('  1------输入')
    print('  2------输出')
    print('  3------查询')
    print('  else---退出')
    print('=====================')
    while True:
        a = int(input("请输入选择(1---3)>>"))
        if a > 0 and a < 4:
            print('--')
        else:
            break
    print('thanks for using!')
if __name__ == '__main__':
    main()