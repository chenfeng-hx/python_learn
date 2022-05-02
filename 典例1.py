# 可以使用字典对数据文件读取存储，如：
dictionary_1 = {"学号":"202022","姓名":"小明","成绩":"98"}
dictionary_2 = {"学号":"202023","姓名":"小红","成绩":"100"}
dictionary_3 = {"学号":"202024","姓名":"小百","成绩":"92"}

# 选用列表类型对数据进行输出
list = [dictionary_1,dictionary_2,dictionary_3]

for i in range(len(list)):    # 对学号进行输出
    print(list[i].get("学号"))

