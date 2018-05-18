import requests # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import os  # 导入os模块

class It(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://www.ithome.com/'  # 要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture'  # 设置要存放的文件目录
        self.proxy = {'http': '42.243.144.3:61202'}
        self.proxys = {'https': '123.56.75.209:3128'}
        self.comment_url ='https://dyn.ithome.com/ithome/getajaxdata.aspx'

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        r.encoding = r.apparent_encoding  # 解决所有网站中文乱码
        return r

    def save_text(self, str, name): # 保存文本
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        os.chdir(self.folder_path)
        print('开始保存今天的文件')
        file_name = name + '.txt'
        f = open(file_name, 'w')
        f.write(str)
        print(file_name,'文本保存成功！')
        f.close()

    def mkdir(self, path):  # 这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

    def get_Article(self):
        print('开始IT之家网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有div标签')
        div = BeautifulSoup(r.text, 'lxml').find('div', class_='new-list-1')
        li = div.find_all('li')
        str = ''
        for a in li:
            title = a.find('span',class_='title').a.text  # 文章标题
            url = a.find('span',class_='title').a['href']  # 文章连接
            date = a.find('span',class_='date').text  # 文章时间
            if date == '今日':  # 只显示今日文章
                str += '文章：' + title + ' ' + url + '\n'
        print(str)
        # self.save_text(str,'IT之家')




it = It()
it.get_Article()