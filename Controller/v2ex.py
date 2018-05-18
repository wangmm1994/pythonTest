import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import os  #导入os模块

class V2ex(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://www.v2ex.com/'  # 要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture'  # 设置图片要存放的文件目录
        self.proxy = {'http': '42.243.144.3:61202'}
        self.proxys = {'https': '123.56.75.209:3128'}

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers, proxies=self.proxys)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
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

    def get_pic(self):
        print('开始V2EX网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有SPAN标签')
        all_a = BeautifulSoup(r.text, 'lxml').find_all('span', class_='item_title')  # 获取网页中的class为cV68d的所有a标签
        for a in all_a: # 循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            print('标题为：',a.string)

beauty = V2ex()  # 创建类的实例
beauty.get_pic()  # 执行类中的方法