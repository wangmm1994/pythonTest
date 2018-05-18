import requests # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import os  # 导入os模块

class QiushiBk(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'http://www.qiushibaike.com/text/page/'  # 要访问的网页地址
        self.proxy = {'http': '42.243.144.3:61202'}
        self.folder_path = 'D:\BeautifulPicture'  # 设置图片要存放的文件目录

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers, proxies=self.proxy)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  # 这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

    def get_qiushibaike(self):
        print('开始糗事百科网页get请求','\n','-----------------------------------------------------------------------')
        r = self.request(self.web_url)
        all_div = BeautifulSoup(r.text, 'lxml').find_all('div', class_='article')
        for div in all_div:
            author = div.find('div',class_='author').h2.string.strip()  # 作者
            text = str(div.find('a',class_='contentHerf').div.span).replace('<span>','').replace('</span>','').strip().replace('<br/>','\n')  # 内容
            stats = div.find('div',class_='stats')  # 笑脸评论数
            vote = stats.find('span',class_='stats-vote').i.string  # 笑脸评论数
            comment = stats.find('span',class_='stats-comments').a.i.string  # 笑脸评论数
            print(author,':',vote,'好笑 ',comment,'评论:')
            print(text,'\n','-----------------------------------------------------------------------')
beauty = QiushiBk()  # 创建类的实例
beauty.get_qiushibaike()  # 执行类中的方法