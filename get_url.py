import json
import requests
from bs4 import BeautifulSoup

# 用于被Crawler继承
class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 记录crawl开头的方法数量
        count = 0
        # 记录crawl开头的方法名
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

class Crawler(object,metaclass=ProxyMetaclass):

    # 传入方法名
    # 返回ip:端口号
    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies
        
    # 获取代理66
    def crawl_daili66(self):
        page_count = 34
        start_url = 'http://www.66ip.cn/areaindex_{}/1.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            res = requests.get(url=url)
            soup = BeautifulSoup(res.text,'html.parser')
            for x in soup.select('.container table tr'):
                ip = x.select('td:nth-child(1)')[0].string
                port = x.select('td:nth-child(2)')[0].string
                if ip != 'ip':
                    yield ':'.join([ip, port])

    # 获取89id
    def crawl_89ip(self):
        page_count = 60
        start_url = 'http://www.89ip.cn/index_{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            res = requests.get(url=url)
            soup = BeautifulSoup(res.text,'html.parser')
            for x in soup.select('.layui-table tbody tr'):
                ip = x.select('td:nth-child(1)')[0].string.strip()
                port = x.select('td:nth-child(2)')[0].string.strip()
                yield ':'.join([ip, port])

    # 获取西刺
    def crawl_xici(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        page_count = 50
        start_url = 'https://www.xicidaili.com/nn/{}'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            res = requests.get(url=url,headers=headers)
            soup = BeautifulSoup(res.text,'html.parser')
            for x in soup.select('.odd'):
                ip = x.select('td:nth-child(2)')[0].string
                port = x.select('td:nth-child(3)')[0].string
                yield ':'.join([ip, port])

    # 获取快代理
    def crawl_kuaidaili(self):
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        page_count = 100
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            res = requests.get(url=url)
            soup = BeautifulSoup(res.text,'html.parser')
            for x in soup.select('.table-striped tbody tr'):
                ip = x.select('td:nth-child(1)')[0].string
                port = x.select('td:nth-child(2)')[0].string
                yield ':'.join([ip, port])