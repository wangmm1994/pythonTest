import requests # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import re


class BeautifulPicture():

    def __init__(self):  # 类的初始化操作
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
                        ,"Cookie":"__cfduid=dd978906aeebe719b5c089376237555c81525694179; __utma=145524284.46094123.1525694181.1525694181.1525694181.1; __utmb=145524284.0.10.1525694181; __utmc=145524284; __utmz=145524284.1525694181.1.1.utmcsr=s2.t7k.space|utmccn=(referral)|utmcmd=referral|utmcct=/; CLIPSHARE=oamddhlq02c8aie4n5e2viebb7; show_msg=1; __51cke__=; __dtsu=D9E9B66BF03EF05A8761D50902FEBFA0; remainclosed=1; 91username=91%E4%B8%9D%E8%A2%9C%E5%A4%A7%E8%89%B2%E7%8B%BC; level=1; DUID=89e3VTVt%2FI3osr8rcBovCCvGS%2BTqSlC4lI5kvhBq7rXfWVVn; USERNAME=7fab7Y%2Bap%2BhV%2FLQrR1FKTUDjnO26WSXaX%2F%2BD24Me0l%2BO57Z%2FHu97wDF6PqUQvg; user_level=1; EMAILVERIFIED=no; watch_times=8; __tins__3878067=%7B%22sid%22%3A%201525696219232%2C%20%22vd%22%3A%209%2C%20%22expires%22%3A%201525698225317%7D; __51laig__=22"
                        ,"Accept-Language": "zh-CN,zh;q=0.9"}  #给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'http://92.91p25.space/v.php?next=watch'  # 要访问的网页地址
        self.proxy = {'http': '42.243.144.3:61202'}

    def get_url(self):
        print('开始获取视频请求')
        r = self.request(self.web_url)
        all_div = BeautifulSoup(r.text, 'lxml').find_all('div',class_='listchannel')
        print('一共查找了', len(all_div), '视频')
        for video in all_div:
            title = video.a.img['title']
            url = video.a['href']
            info = video.find_all('span',class_='info')
            timel = info[0].nextSibling.strip()
            create = info[1].nextSibling.strip()
            autho = info[2].nextSibling.strip()
            video_url = self.get_video_url(url)
            print('title',title,'时长',timel,'创建时间：',create,'作者：',autho,'\n','url:',video_url)

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        r.encoding = 'utf-8'  # 解决中文乱码
        return r

    def get_video_url(self,url):
        r = self.request(url)
        all_div = BeautifulSoup(r.text, 'lxml').find('div',class_='example-video-container')
        return all_div.source['src']

beauty = BeautifulPicture()  # 创建类的实例
beauty.get_url()  # 执行类中的方法