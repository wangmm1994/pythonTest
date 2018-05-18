import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import time  # 导入时间 模块
import pymysql  # 导入pymysql 模块
import contextlib  # 导入contextlib 模块


class Iqshw(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://www.iqshw.com'  # 要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture'  # 设置图片要存放的文件目录
        self.proxy = {'http': '42.243.144.3:61202'}

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers, proxies=self.proxy)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        print('iqshw编码:',r.apparent_encoding)
        r.encoding = 'gb18030'  # 解决所有网站中文乱码
        return r

    def get_youhui(self):
        print('开始IQSHW网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有SPAN标签')
        div = BeautifulSoup(r.text, 'lxml').find('div', class_='news-comm-wrap')  # 获取网页中的class为cV68d的所有a标签
        all = div.find_all('li')
        str = ''
        date = time.strftime("%m-%d") # 获取当前日期
        dao = IqshwDao()
        print ('date:',date)
        for a in all:
            if a.span and a.span.text == date:
                href = self.web_url + a.a['href']
                str = str + a.a.text + '    ' + href + ' 时间：' + a.span.text + '\n'
                # 放入数据库
                dao.insert_iqshw(a.a.text, href, a.span.text)
        print(str)

'''
iqshw数据库操作
每次都连接关闭很麻烦，使用上下文管理，简化连接过程
定义上下文管理器，连接后自动关闭连接   
'''
class IqshwDao(object):
    @contextlib.contextmanager
    def mysql(self,host='127.0.0.1', port=3306, user='root', passwd='1234', db='python', charset='utf8'):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield cursor
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    # 查询sql
    def query_iqshw(self):
        with self.mysql() as cur:
            sql = "select * from iqshw"
            cur.execute(sql)
            for r in cur.fetchall():
                print(r)

    # 查询数据酷是否有此数据
    def is_repetitions(self,title,url):
        with self.mysql() as cur:
            sql = "select * from iqshw where title = '%s' and url = '%s'" % (title, url)
            cur.execute(sql)
            if len(cur.fetchall()) > 0:
                return 1
            else:
                return 2

    # 添加sql
    def insert_iqshw(self,title, url,time):
        with self.mysql() as cur:
            if self.is_repetitions(title, url) == 2:
                sql = "insert into iqshw(title,url,time) values('%s','%s','%s')" % (title, url, time)
                cur.execute(sql)
                print('添加', title, '成功')
            else:
                print(title, '数据已存在！')

iq = Iqshw()
iq.get_youhui()