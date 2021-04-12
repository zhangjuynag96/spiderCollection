import requests

url = 'https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=9ab182b200050ef5&wd=python&pn=10&oq=python&tn=baiduhome_pg&ie=utf-8&usm=4&rsv_idx=2&rsv_pq=9ab182b200050ef5&rsv_t=9911Qm0KL8HQNp%2BiAZni0eZtA5Bj6dE0apGisIvcEe0kIZErg8RbiSFiqxIu0OfoM20h&rsv_page=1&bs=python&rsv_sid=33818_33257_33273_31253_33757_33714_26350&_ss=1&clist=&hsug=python%20%E5%8F%91%E9%80%81wsdl&f4s=1&csor=6&_cr1=28544'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
resp = requests.get(url, headers=headers)
print(resp)