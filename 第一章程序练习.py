# 字符串拼接，接收用户输入的两个字符串，将他们组合后输出
# str1 = input("请输入一个人的名字：")
# str2 = input("请输入一个国家的名字：")
# print("世界那么大,{}想去{}看看".format(str1,str2))

# 整数序列求和。用户输入一个正整数N，计算从1到N（包含1和N）相加之后的结果
# n = input("请输入整数N：")
# sum = 0
# for i in range(int(n)):
#     sum += i + 1
# print("1到N求和结果：",sum)

# 九九乘法表输出。工整打印输出常用的九九乘法表，格式不限。
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={:2}".format(j,i,i*j),end=' ')
#     print('')

# 计算1！+2！+3！+……+10！的结果。
# sum,tmp = 0,1
# for i in range(1,11):
#     tmp *= i
#     sum += tmp
# print("运算结果是：{}".format(sum))

# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个；第二天
# 早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半多一个。到
# 第五天早上再想吃时，看见只剩一个桃子了。编写程序计算猴子第一天共摘了多少桃子
# n = 1
# for i in range(5,0,-1):
#     n = (n+1)<<1
# print(n)

# 健康食谱输出。列出5种不同食材，输出它们可能组成的所有菜式名称。
# diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
# for x in range(0,5):
#     for y in range(0,5):
#         if not(x==y):
#             print("{}{}".format(diet[x],diet[y]))

# 五角星的绘制：绘制一个红色的五角星图形
from turtle import *
fillcolor("red")          #fill：填充
begin_fill()
while True:
    forward(200)
    right(144)
    if abs (pos()) < 1:
        break
end_fill()
done()

# 太阳花的绘制：绘制一个太阳花的图形
# from turtle import *
# color('red','yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()




