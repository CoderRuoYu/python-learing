import random
num = random.randint(1, 100)
cn = 0
guess_num = -1
while 1:
    guess_num = int(input("请输入您猜的数字："))
    cn += 1
    if guess_num == num:
        break
    elif guess_num > num:
        print("您猜大了")
    else:
        print("您猜小了")

print("恭喜您猜对了，一共猜测了%s次" % cn)