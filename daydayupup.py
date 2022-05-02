# 每天进步千分之一，一年进步多少，每天娱乐千分之一，一年退步多少

# dayup = pow(1.001,365)
# daydown = pow(0.999,365)
# print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))

# 千分之五和百分之一的力量

# dayfactor = 0.005      #可以修改为百分之一
# dayup = pow(1+dayfactor,365)
# daydown = pow(1-dayfactor,365)
# print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))

# 工作日的力量，工作日进步百分之一，休息日退步百分之一，一年后结果如何：

# dayup = 1.0
# dayfactor = 0.01
# for i in range(365):
#     if i%7 in [6,0]:
#         dayup *= 1 - dayfactor
#     else:
#         dayup *= 1 + dayfactor
#
# print("工作日的力量：{:.2f}".format(dayup))

# 工作日的努力：
# A：每天进步百分之一，一年   B:工作5天休息2天，如何做到与A相同？


