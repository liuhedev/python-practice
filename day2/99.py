# 99乘法表
i=1 
# 控制行
while(i<=9):
    # 控制列
    j=1
    while(j<=i):
        print("%d*%d=%d "%(i,j,j*j),end="")
        j+=1
    i+=1
    print("")
