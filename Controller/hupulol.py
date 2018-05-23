import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块

class  Hupulol(object):
    def __init__(self):
        self.article_url = 'https://bbs.hupu.com/lol'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.base_url = 'https://bbs.hupu.com'
    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        r.encoding = r.apparent_encoding  # 解决所有网站中文乱码
        return r

    def get_title(self):
        print('开始虎扑lol网页get请求')
        print('-------------------------------------------------------------------------------------------')
        r = self.request(self.article_url)
        div = BeautifulSoup(r.text, 'lxml').find('ul', class_='for-list')
        li = div.findAll("li")
        for a in li:
            title = a.find('a',class_='truetit').text  # 文章标题
            url = self.base_url + a.find('a',class_='truetit')['href']  # url
            autho = a.find('a',class_='aulink').text
            date = a.find('div',class_='author').findAll('a')[1].text
            ansour = a.find('span',class_='ansour').text
            print(autho,'  ',date,'   回复/浏览  ', ansour ,'\n',title,'   ',url)
            print('-------------------------------------------------------------------------------------------')
hupulol = Hupulol()
hupulol.get_title()