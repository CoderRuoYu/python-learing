a = {
     "王力宏":{"部门": "科技部", "工资": 1000, "级别": 1},
     "小兰":{"部门": "技术部", "工资": 2000, "级别": 2},
     "阿水":{"部门": "财务部", "工资": 3000, "级别": 3}
    }
print(a)

for key in a.keys():
    if a[key]["级别"] == 1:
        a[key]["级别"]=a[key]["级别"]+1
        a[key]["工资"]=a[key]["工资"]+1000
print(a)

