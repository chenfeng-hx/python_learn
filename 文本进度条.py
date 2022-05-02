# 进度条过程性展示
# import time
# scale = 10
# print("执行开始".center(scale//2),'-')
# for i in range(scale+1):
#     a = '*' * i
#     b = '-' * (scale - i)
#     c = i / scale * 100
#     print("{:^3.0f}%:[{}->{}]".format(c,a,b))
#     time.sleep(0.1)
# print("\n"+"执行结束".center(scale//2,'-'))

# 进度条单行动态刷新
import time
for i in range(101):
    print("\r{:^3}%".format(i), end='')
    time.sleep(0.1)
print("执行结束")