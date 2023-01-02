import random
num = random.randint(1,10)
print(num)
num1 = 0
num1 = int(input("请输入您猜测的数字："))
if num1 == num:
    print("恭喜您猜对了！")
else:
    if num1 > num:
        num1 = int(input("您猜大了，请重新输入："))
        if num1 == num:
            print("恭喜您猜对了！")
        else:
            if num1 > num:
                num1 = int(input("您猜大了，请重新输入："))
                if num1 == num:
                    print("恭喜您猜对了！")
                else:
                    print("Sorry,您全部猜错了。")
            else:
                num1 = int(input("您猜小了，请重新输入："))
                if num1 == num:
                    print("恭喜您猜对了！")
                else:
                    print("Sorry,您全部猜错了。")

    else:
        num1 = int(input("您猜小了，请重新输入："))
        if num1 == num:
            print("恭喜您猜对了！")
        else:
            if num1 > num:
                num1 = int(input("您猜大了，请重新输入："))
                if num1 == num:
                    print("恭喜您猜对了！")
                else:
                    print("Sorry,您全部猜错了。")
            else:
                num1 = int(input("您猜小了，请重新输入："))
                if num1 == num:
                    print("恭喜您猜对了！")
                else:
                    print("Sorry,您全部猜错了。")