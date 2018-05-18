from bs4 import BeautifulSoup
import requests

url = 'http://ip.chinaz.com/'
proxies = {
    'http': '42.243.144.3:61202',
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36 Qiyu 2.1.0.0'}  # 给请求指定一个请求头来模拟chrome浏览器

r = requests.get(url, headers=headers,proxies=proxies)
soup = BeautifulSoup(r.text, 'lxml')
parent_node = soup.find(class_="IpMRig-tit")
for i in parent_node.find_all('dd'):
    print(i.get_text())