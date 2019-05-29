import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块



class Hey(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'http://heyav.tv/web/list.php?&now_page=1'  # 要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture'  # 设置图片要存放的文件目录
        self.base_url = 'http://heyav.tv/web/'
        self.pic_url = 'http://heyav.tv'
    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        r.encoding = r.apparent_encoding  # 解决所有网站中文乱码
        return r

    def get_youhui(self):
        print('开始网页get请求###')
        r = self.request(self.web_url)
        print('开始获取所有SPAN标签')
        div = BeautifulSoup(r.text, 'lxml').find('ul', class_='mvlist')  # 获取网页中的class为cV68d的所有a标签
        all = div.find_all('li')
        print('一共获取了',len(all),'条记录')
        for a in all:
            title = a.h3['title']
            type = a.find('div',class_='mvtagbox').string
            url = self.base_url + a.find('a',class_='listimgbox')['href']
            time = a.find('p',class_='pic-date').a.string
            print('标题:',title,'类型:',type,'上架时间:',time,'\n','url:',url)


hi = Hey()
hi.get_youhui()
