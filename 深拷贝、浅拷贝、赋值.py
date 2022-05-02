list_1 = ['hello','python',123,'中国']   # 创建一个列表

list_copy_1 = list_1.copy()
list_copy_2 = list_1

list_1.pop()   # 删去列表的最后一个元素
print('list_1:',list_1)      # 删去后的原列表
print('list_copy_1:',list_copy_1)   # 打印deepcopy
print('list_copy_2:',list_copy_2)   # 打印shallowcopy
