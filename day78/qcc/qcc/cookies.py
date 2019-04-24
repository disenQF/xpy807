import random

cookies = [
    'acw_tc=7cc1e21515560926397044713e60bedde81222830d2089dcccc8383119; '
    'QCCSESSID=52spbi8f4p2a8q1gvd1lmpoft6; '
    'zg_did=%7B%22did%22%3A%20%2216a4e5962ba202-00179bbdb4c25c-36697e04-fa000-16a4e5962bbe8%22%7D; '
    'UM_distinctid=16a4e596642197-07384a96c30bf8-36697e04-fa000-16a4e5966443b8; '
    'CNZZDATA1254842228=1170326332-1556091700-%7C1556091700;'
    ' Hm_lvt_3456bee468c83cc63fb5147f119f1075=1556092643;'
    ' _uab_collina=155609264499524039732715; hasShow=1; '
    'zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201556092642009%2C%22updated%22%3A%201556093263165%2C%22info%22%3A%201556092642030%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22093f6d45452e9aad1e822e1fcf969ef0%22%7D; '
    'Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1556093265',

]

def get_cookie():
    # 随机选择一个cookie
    cookies_txt = random.choice(cookies)

    # 将cookie转成字典
    cookie_list = [tuple(cookie.split('=')) for cookie in  cookies_txt.split(';')]
    return { key:value for key, value in cookie_list }


if __name__ == '__main__':
    print(get_cookie())