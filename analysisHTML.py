import requests
from bs4 import BeautifulSoup

#给请求指定一个请求头来模拟chrome浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'} 

# 向目标url地址发送get请求，返回一个response对象
web_url = 'https://unsplash.com'
r = requests.get(web_url, headers=headers)
# 获取网页中的class为cV68d的所有a标签
all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_='_2Mc8_')

for a in all_a:
  print(a['title'])