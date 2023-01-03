num = 11
cn = 0
for x in range(1,num):
    if x % 2 ==0:
        cn += 1
print(f"1到{num}(不含{num}本身)范围内，有{cn}个偶数")