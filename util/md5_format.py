from hashlib import md5


def md5_code(txt):
    m = md5()
    m.update(txt.encode())
    return m.hexdigest()  # 16进制的数字表示的字符串-32位长度


if __name__ == '__main__':
    print(md5_code('https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=591271875,3190619325&fm=58&s=188AAF5F9EB578111A5DCB7E0300C070&bpow=121&bpoh=75'))