import time
# import datetime

def calculate_function_run_time(func):

    def call_fun(*args, **kwargs):
        start_time = time.time()                                     
        #time.time()返回当前时间的时间戳（1970纪元后经过的浮点秒数）
        f = func(*args, **kwargs)
        #程序运行
        end_time = time.time()
        print('%s() run time：%s ms' % (func.__name__, int(1000*(end_time - start_time)))) 
        #以毫秒为单位显示
        return f
    return call_fun

# 尝试单层 失败= = func()参数为空 运行会报错  #args未被定义
# def calculate_function_run_time(func):
#     start_time = time.time()                                     
#     #time.time()返回当前时间的时间戳（1970纪元后经过的浮点秒数）
#     f = func()
#     #程序运行
#     end_time = time.time()
#     print('%s() run time：%s ms' % (func.__name__, int(1000*(end_time - start_time)))) 
#     #以毫秒为单位显示
#     return f


@calculate_function_run_time
# == test1 = calculate_function_run_time(test1)
def test1():
    for i in range(100000):
        i = i +1

@calculate_function_run_time
def test2():
    for i in range(10000000):
        i = i +1


if __name__ == "__main__":
# 防止被import时运行
    test1()
    test2()


# 函数装饰器用于修改和补足其他函数的功能，使代码更简洁