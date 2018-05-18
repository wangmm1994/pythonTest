import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class ItCommont(object):
    def __init__(self):
        self.article_url = 'https://www.ithome.com/'
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0 Qiyu 2.1.0.0'

    def scroll_down(self, driver, times):
        for i in range(times):
            time.sleep(3)  # 等待3秒（时间可以根据自己的网速而定），页面加载出来再执行下拉操作
            print("开始执行第", str(i + 1), "次下拉操作")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 执行JavaScript实现网页下拉倒底部
            print("第", str(i + 1), "次下拉操作执行完毕")
            print("第", str(i + 1), "次等待网页加载......")

    # 获取文章url
    def get_article(self):
        print('开始IT之家网页get请求')
        r = self.request(self.article_url)
        print('开始获取所有div标签')
        div = BeautifulSoup(r.text, 'lxml').find('div', class_='new-list-1')
        li = div.find_all('li')
        str = ''
        for a in li:
            title = a.find('span', class_='title').a.text  # 文章标题
            url = a.find('span', class_='title').a['href']  # 文章连接
            date = a.find('span', class_='date').text  # 文章时间
            if date == '今日':  # 只显示今日文章
                str += '文章：' + title + ' ' + url + '\n'
        print(str)

    def request(self, url):  # 返回网页的response
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        r.encoding = r.apparent_encoding  # 解决所有网站中文乱码
        return r

    # 获取文章下的评论
    def get_comment(self):
        print('开始网页it之家评论请求')
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (self.userAgent)
        driver = webdriver.PhantomJS(desired_capabilities=dcap)  # 使用selenium通过PhantomJS来进行网络请求
        driver.get('https://www.ithome.com/html/it/358862.htm')
        self.scroll_down(driver=driver, times=2)  # 执行网页下拉到底部操作，执行5次
        driver.switch_to.frame('ifcomment')  # it之家评论在id为ifcomment的iframe框架中，切换到该框架
        hot_comment = BeautifulSoup(driver.page_source, 'lxml').find('ul', id='ulhotlist')  # 热门评论
        comment = BeautifulSoup(driver.page_source, 'lxml').find('ul', id='ulcommentlist')  # 普通评论
        if hot_comment is not None:
            print('总共', len(hot_comment.find_all('li')), '热门评论--------------------------------------')
            for hot in hot_comment.find_all('li'):
                commont = hot.p.string  # 评论
                author = hot.find('span', class_='nick').a.string  # 用户
                phone = ''
                if hot.find('span', class_='mobile') is not None:
                    phone = hot.find('span', class_='mobile').a.string  # 手机
                where = hot.find('span', class_='posandtime').string  # 时间地点
                floor = hot.find('strong', class_='p_floor').string  # 几搂
                zhichi = hot.find('div', class_='zhiChi')
                more_commont = ''
                for i, text in enumerate(zhichi.find('span', class_='comm_reply').a):
                    if i == 0:
                        more_commont = text
                zan = zhichi.find('a', class_='s').string
                fan = zhichi.find('a', class_='a').string
                print('昵称:', author, '手机:', phone, where, floor, '\n', commont, '\n', more_commont, '       ', zan, fan,
                      '\n''-----------------------------------------------')
        else:
            print('该文章还没有热门评论！')
        print('全部评论：', len(comment.find_all('li', class_='entry')), '条--------------------------------------')
        for hot in comment.find_all('li', class_='entry'):
            commont = hot.p.string  # 评论
            author = hot.find('span', class_='nick').a.string  # 用户
            phone = ''
            if hot.find('span', class_='mobile') is not None:
                phone = hot.find('span', class_='mobile').a.string  # 手机
            where = hot.find('span', class_='posandtime').string  # 时间地点
            floor = hot.find('strong', class_='p_floor').string  # 几搂
            zhichi = hot.find('div', class_='zhiChi')
            zan = zhichi.find('a', class_='s').string
            fan = zhichi.find('a', class_='a').string
            print('昵称:', author, ' 手机:', phone, where, floor, '\n', commont, '\n', '       ', zan, fan,
                  '\n''-----------------------------------------------')


it = ItCommont()
it.get_comment()
