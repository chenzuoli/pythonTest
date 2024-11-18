# -*- coding: utf8 -*-

"""
爬取csdn文章

pip install selenium
pip install beautifulsoup4
pip install markdownify
pip install webdriver-manager
"""

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    """
    主方法
    """
    cookie = "uuid_tt_dd=xxxxxxxx-1727360428521-705637; fid=20_26587497275-xxxxxxxx-502018;  dc_tos=skzhb8"
    csdn_url = "https://bizapi.csdn.net/blog/phoenix/console/v1/article/list?page=%s&pageSize=%s"
    accept = "application/json, text/plain, */*"
    referer = "https://mp.csdn.net/mp_blog/manage/article"
    x_ca_key = "xxxxxxxx"
    x_ca_nonce = "6704920d-xxxx-48de-a5c9-9240ddcc0014"
    x_ca_signature = "xxxxxxxxxxxx/uT8SBd9Uvn2ro="
    x_ca_signature_headers = "x-ca-key,x-ca-nonce"
    page = 1
    page_size = 20
    crawl_url = csdn_url % (page, page_size)
    headers = {
        "cookie": cookie,
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://mp.csdn.net/mp_blog/manage/article",
        "Access-Control-Max-Age": "86400",
        "X-Ca-Key": x_ca_key,
        "X-Ca-Nonce": x_ca_nonce,
        "X-Ca-Signature": x_ca_signature,
        'X-Ca-Signature-Headers': x_ca_signature_headers
    }
    print(crawl_url)
    response = requests.get(crawl_url, headers=headers)
    print(response.status_code, response.text)


def get_article_by_chrome():
    """
    通过selenium获取csdn文章内容
    通过beautifulsoup4解析html
    通过markdownify解析文章html内容为markdown
    """

    csdn_article_url = 'https://blog.csdn.net/xuezhe5212/article/details/140344334'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.page_load_strategy = 'eager'  # 加快页面的加载速度
    chrome_options.add_argument("--no-sandbox")

    from selenium.webdriver.chrome.service import Service
    service = Service(executable_path="/usr/bin/google-chrome")

    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get(csdn_article_url)
    source_html = chrome.page_source
    soup = BeautifulSoup(source_html, 'html.parser')
    title = soup.find('title').get_text(strip=True)
    content_html = soup.find('div', {'id': 'content_views'})
    content = md(str(content_html))
    print(title, content)


def get_article_by_firefox():
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    web_url = 'https://blog.csdn.net/xuezhe5212/article/details/140344334'
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # 不打开浏览器
    options.browser_version = 'stable'
    options.page_load_strategy = 'eager'
    # profile_path = "C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\kdzv5ez8.default-release-1"
    # profile = webdriver.FirefoxProfile(profile_directory=profile_path)
    # firefoxdriver_path = "D:\\Firefox\\geckodriver-v0.33.0-win64\\geckodriver.exe"
    firefoxdriver_path = "/home/lezhifu/geckodriver"
    service = Service(executable_path=firefoxdriver_path)
    firefox_path = "/home/lezhifu/firefox/firefox"
    options.binary_location = firefox_path
    print('connecting firefox webbrowser.')
    firefox = webdriver.Firefox(service=service, options=options)
    # options.profile = profile
    # firefox = webdriver.Firefox(options=options)
    firefox.get(web_url)
    print(f'connected web url: {web_url}')
    source_html = firefox.page_source
    soup = BeautifulSoup(source_html, 'html.parser')
    title = soup.find('title').get_text(strip=True)
    content_html = soup.find('div', {'id': 'content_views'})
    content = md(str(content_html))
    print(title, content)


if __name__ == '__main__':
    # main()
    # get_article_by_chrome()
    get_article_by_firefox()
