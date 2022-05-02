a,b =0,1
while a < 1000:
    print(a, end=',')
    a,b = b,a+b           #根据这个式子可以探究python存储原理