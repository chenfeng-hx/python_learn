import turtle
turtle.title('自动轨迹绘制')
turtle.setup(800,600,0,0)
turtle.pencolor('red')
turtle.pensize(5)
# 数据读取
datels = []
f = open("E:\\编码呢\\Pycharm\\pythonlearn\\txt文件\\date.txt")
for line in f:
	line = line.replace("\n","")
	datels.append(list(map(eval,line.split(","))))
f.close()
# 自动绘制
for i in range(len(datels)):
	turtle.pencolor(datels[i][3],datels[i][4],datels[i][5])
	turtle.fd(datels[i][0])
	if datels[i][1]:
		turtle.right(datels[i][2])
	else:
		turtle.left(datels[i][2])