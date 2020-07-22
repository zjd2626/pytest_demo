import time


def outer(func):
    print("*"*50)
    def inner(name):
        func(name)
    return inner

@outer
def say(name):
    print("my name is %s." %name)


say("zjd")


def fib(n):
    a,b,counter = 1,1,1
    while counter<=n:
        yield a
        a, b = b, a + b
        counter +=1


print([x for x in fib(12)])


#从第三个月开始，每个月兔子对数为前两个月兔子对数之和，其实就是fibonacci数列
def fun(n):
    if n==1 or n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)

print("一年后一共有%d对兔子" % fun(12))
