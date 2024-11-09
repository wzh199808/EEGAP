import Crypto.Util.number as numb
import random


# 求逆的函数，之前的版本用python2写的，这次用的python3，只把整除符号改了一下
def oj(a, n):
    a = a % n
    s = [0, 1]
    while a != 1:
        if a == 0:
            return 0
        q = n // a
        t = n % a
        n = a
        a = t
        s += [s[-2] - q * s[-1]]
    return s[-1]


# max_length 为p的长度，同时也是秘密的最大长度
# secret_is_text =0 默认输入时文本， 非0时认为是数字
# p 默认为0， 会根据max_length 自动生成，不为0时直接使用，需要保证p为素数， 函数内没有素性检验
def create(max_length=513, secret_is_text=0, p=0):
    if not p:
        p = numb.getPrime(max_length)

    w = 6#int(input("请输入秘密保存人数："))
    t = 4#int(input("请输入秘密恢复所需人数："))
    while not (t > 0 and t <= w):
        t = 8#int(input("请重新输入："))
    s = 100 #input("请输入你的秘密:")

    if secret_is_text:
        s = numb.bytes_to_long(s.encode("utf-8"))
    else:
        try:
            s = int(s)
        except Exception as e:
            s = numb.bytes_to_long(s.encode("utf-8"))

    x_list = list()
    a_list = list()
    i = w
    while i > 0:
        x = random.randint(p // 2, p)  # 该范围没有特定限制，如果想让xi,yi取小一点儿的话可把范围写小点儿，但是要大于w
        if x not in x_list:
            x_list.append(x)
            i -= 1

    for a in range(t):
        a_list.append(random.randint(p // 2, p))  # 同上

    result = list()
    for x in x_list:
        y = s
        for a_n in range(t):
            a = a_list[i]
            y += a * pow(x, i + 1, p)
        result.append([x, y])
    return t, p, result


# get_text=1 默认恢复为字符串，若想得到数字填0
def restore(p, information, get_text=1):

    x_list = list()
    y_list=list()
    for x, y in information:
        x_list.append(x)
        y_list.append(y)

    s = 0
    for x_i in range(len(x_list)):
        tmp_num = y_list[x_i]
        x_i_j = 1
        for x_j in range(len(x_list)):
            if x_i != x_j:
                tmp_num = tmp_num * (0 - x_list[x_j]) % p
                x_i_j *= x_list[x_i] - x_list[x_j]
        tmp_num = tmp_num * oj(x_i_j, p) % p
        s += tmp_num

    s = s % p
    print(s)
    if get_text:
        try:
            s = numb.long_to_bytes(s)
            s = s.decode("utf-8")
        except Exception as e:
            print(e)

    return s


t, p, result = create()             #result为秘密碎片的列表
print(result)
print(type(result[0][1]))
result[0][1]+=100
result[1][1]-=100
print(restore(p, result[:t]))     #这里我取了result的前t个，实际中可以取任意t个。




