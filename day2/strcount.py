str='hello world'
dict={}

count = 0
for s in str :
    if s in dict:
        #如果存在当前key，value+1
       dict[s]+=1
    else:
       dict[s]=1

print(dict)

