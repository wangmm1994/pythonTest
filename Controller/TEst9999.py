import requests # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import os  # 导入os模块
import re

class BeautifulPicture():

    def __init__(self):  # 类的初始化操作
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  #给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'http://g.91p11.space/forumdisplay.php?fid=19&page=2'  # 要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture\\'  # 设置图片要存放的文件目录
        self.proxy = {'http': '42.243.144.3:61202'}
    def get_url(self):
        print('开始标题get请求')
        r = self.request(self.web_url)
        regexp_url = re.compile("thread*")  # 通过正则查找标签
        all_tbody = BeautifulSoup(r.text, 'lxml').find_all('tbody')  # 获取网页中的class为cV68d的所有a标签
        print('一共查找了', len(all_tbody), '记录')
        for tbody in all_tbody:  # 循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            span = tbody.tr.th.find('span', id=regexp_url)  # a标签中完整的style字符串
            title = span.a.string  # 文章标题
            url = 'http://g.91p11.space/' + span.a['href']
            print(title, 'url:', url)
            self.get_pic(url)

    def get_pic(self,pic_url):
        print('开始获取图片get请求')
        r = self.request(pic_url)
        print('开始获取所有a标签')
        regexp_pic = re.compile("attachments*")  # 通过正则查找标签
        all_a = BeautifulSoup(r.text, 'lxml').find_all('img', file=regexp_pic)  # 获取网页中的class为cV68d的所有a标签
        title = BeautifulSoup(r.text, 'lxml').find('div',id='threadtitle').h1.string
        print('开始创建文件夹',title)
        self.mkdir(self.folder_path+title)  # 创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path+title)   # 切换路径至上面创建的文件夹
        print('一共查找了',len(all_a),'图片')
        i = 1
        for a in all_a:  # 循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            img_str = a['file']  # a标签中完整的style字符串
            print('图片的src是：', img_str)
            img_url = 'http://g.91p11.space/' + img_str  # 使用Python的切片功能截取双引号之间的内容
            print('图片的url是：', img_url)
            img_name = i
            print('保存的文件名：',img_name)
            self.save_img(img_url, img_name)  # 调用save_img方法来保存图片
            i = i + 1

    def save_img(self, url, name):  # 保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        file_name = str(name) + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name,'图片保存成功！')
        f.close()

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers, proxies=self.proxy)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        r.encoding = 'utf-8'  # 解决中文乱码
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

beauty = BeautifulPicture()  # 创建类的实例
beauty.get_url()  # 执行类中的方法