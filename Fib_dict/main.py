# 初始化
flag = False
a, b = 1, 1
Fib = [1]
'''
多行注释
基本输入输出
类型转换
分支 循环
list方法
复合赋值 
'''
s = input("give me an positive integer:")
n = int(s)
if n < 1:
    print("integer should be positive!")
else:
    while b <= n:
        Fib.append(b)
        a, b = b, a + b

print('Fibonacci list no larger than', n, 'is:')
print(Fib)
print(len(Fib))


# 字典推导式
print('Fibonacci dictionary no larger than', n, 'is:')
Fib_dict = {i+1: Fib[i] for i in range(0, len(Fib))}
print(Fib_dict)

