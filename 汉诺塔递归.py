# -*- coding:UTF-8 -*-
"""
作者:尘封
日期:2022年04月10日
"""

"""
有 n 根柱子，确定圆盘是从哪根源柱子转移到哪根目标柱子上，
中间又经过了哪根中间柱子，第一个参数是圆盘的数量，第二个
参数是源柱子，第三个参数是目标柱子，第四个参数是中间柱子 
"""

count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))   # 输出时从哪一个源柱子到那一个目标柱子
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)

hanoi(10,'A','B','C')



