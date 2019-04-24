import random

# ua池
ua = [
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
  'Chrome/73.0.3683.103 Safari/537.36',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 '
  'Safari/605.1.15'
]

# cookie 池
cookies = [
    'UM_distinctid=16a2f84014e8f-0eec4b63007f8b-366e7e04-75300-16a2f84014f716; CNZZDATA300636=cnzz_eid%3D194096366-1555579563-http%253A%252F%252Fsc.chinaz.com%252F%26ntime%3D1555579563; ASP.NET_SessionId=frnxl1jedgzkgwzab34mechj; Wbm_QZoneV2SDK_my_login=0B223C81C0F98D78C59CDBD0B55BA45A77C01907F85286B3EDAA7649A0D1D628721B50ECE1C1729CD710D5FFED1D43E5A0D9100AD8E542293E28314A156739058F2952F569A6C887; CzScCookie=userid=2944460&gradeid=1&isvip=0&UserName=qq_20190418173457190&Money=0.0000&Token=EB61D4F67E99328C509FF78D62CA9BA2'
]

def get_ua():
    return random.choice(ua)

def get_headers():
    headers = {
        'User-Agent': random.choice(ua),
        # 'Cookie': random.choice(cookies)
    }

    return headers


if __name__ == '__main__':
    print(get_headers())