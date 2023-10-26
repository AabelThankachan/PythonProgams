def fun1():
    x=100
    def fun2():
        x=200
        def fun3():
            nonlocal x
            x=300
        print("before calling fun3:"+str(x))
        print("calling fun3 now:")  
        fun3()
        print("after calling fun2:"+str(x))
    x=50
    fun2()
    print("x in main:"+str(x))
x=150
fun1()
print("x in main:"+str(x))
        
            
                  
