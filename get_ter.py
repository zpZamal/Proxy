from save import RedisClient
from get_url import Crawler
import asyncio
import aiohttp
import time

POOL_UPPER_THRESHOLD = 10000

# 将数据传入redis
class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()
 
    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
 
    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            # 获取代理网站数量并循环
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                # 代理网站方法名
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 传入方法名，返回ip:端口号
                proxies = self.crawler.get_proxies(callback)
                # 数据存入redis
                for proxy in proxies: 
                    self.redis.add(proxy)