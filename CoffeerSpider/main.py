from scrapy.cmdline import execute

# 等价于将爬取道德数据导出到items.json文件中
execute("scrapy crawl comment -o items.json".split())
