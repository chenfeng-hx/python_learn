user_dict = {}    # 定义一个空字典
flag = 0
print('1、添加单词'+' '*3+'2、查找单词'+' '*3+'0、退出程序')   # 用户提示信息
while True:
    user = eval(input("请输入您要进行的操作："))   # 用户选择操作类型,用eval函数去引号
    if user == 1:        # 进行添加单词操作
        key = input('请输入您想添加的单词定义(key)：')   # 添加键
        user_dict[str(key)] = str(input('请输入您想为该定义添加的单词(value)：'))   # 添加值
        print('添加操作成功！')
        print(user_dict)
        continue
    elif user == 2:    # 进行查找单词操作
        check_key = input('请输入您想找到的定义(key):')
        for dict_key in sorted(user_dict.keys()):  # 对该用户字典中的所有键的信息排序并查找
            if str(check_key) == str(dict_key):   # 找到相应的键
                flag = 1     # 标志匹配的信息
                break
            else:
                flag = 0     # 标志未匹配的信息
        if flag == 1:
            print('已找到！',check_key,':',user_dict[check_key])   # 返回相应的键值对
        else:
            print('不存在该单词！')
    elif user == 0:
        print('退出程序！')
        break




# dictionary = {}
# flag = 'a'
# pape = 'a'
# off = 'a'
# while flag =='a' or 'c':
#     flag = input('添加或查找单词？(a/c)')
#     if flag =='a':
#         word = input('输入单词(key)')
#         defintion = input('输入的定义值(value)')
#         dictionary[str(word)] = str(defintion)
#         print('添加成功')
#         pape = input('您是否要查找字典(a/0)')
#         if pape =='a':
#             print(dictionary)
#         else:
#             continue
#     elif flag =='c':
#         check_word = input('要查找的单词')
#         for key in sorted(dictionary.keys()):
#             if str(check_word)== key:
#                 print('存在',key,dictionary[key])
#                 break
#             else:
#                 off = 'b'
#             if off =='b':
#                 print('抱歉')
#         else:
#             print('error type')
#             break