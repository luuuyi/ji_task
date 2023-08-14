import os
import re

def remove_number(input_str):
    new_string = ""
    for char in input_str:
        if not char.isnumeric():
            new_string += char
    return new_string

def remove_space(input_str):
    new_string = ""
    for char in input_str:
        if char != " ":
            new_string += char
    return new_string

def remove_url(input_str):
    # https://zhuanlan.zhihu.com/p/593473449
    # import ipdb; ipdb.set_trace()
    input_str = re.sub(r'^(https:\S+)', '', input_str)
    input_str = re.sub(r'[a-zA-Z]+://[^\s]*', '', input_str)
    return input_str

def remove_duplicate_str(str_list):
    assert isinstance(str_list, list)
    data = set()
    for a in [a.strip('\n') for a in str_list]:  # 把读取进来的数据变成列表，再逐个循环读取列表里面的数据（去除开头和结尾的换行）
        if a not in data:  # 判断循环的数据在不在集合里，不在就添加进集合
            data.add(a)
    return list(data)

if __name__ == "__main__":
    input_str = "xxxx xxxx 123 https://baidu.com yyyy"
    
    # No.1
    # input_str = remove_number(input_str)
    # print(input_str)

    # input_str = remove_space(input_str)
    # print(input_str)

    # input_str = remove_url(input_str)
    # print(input_str)

    str_list = [input_str] * 10
    str_list = remove_duplicate_str(str_list)
    print(str_list)