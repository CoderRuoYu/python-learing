def welcome(x):
    print("欢迎来到北京交通大学！请您出示您的健康码以及72小时核酸检测证明，并配合测量体温")
    print(f"体温检测中，您的体温是：{x}",end=',')
    if x <= 37.5:
        print("体温正常请进！")
    else:
        print("需要隔离")


x = float(input())
welcome(x)