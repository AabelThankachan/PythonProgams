count=1
def doTask():
    global count
    for i in(1,2,3):
        count+=1
    doTask()
print(count)#answer32
