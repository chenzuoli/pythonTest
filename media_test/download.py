import requests

base_url = "https://www.isuzu7070.com/ff32cedd-556c-4a9b-98d8-5122b80e7ae4"
uid = 'ff32cedd-556c-4a9b-98d8-5122b80e7ae4'


from httputil import HttpRequestUtil

util = HttpRequestUtil(base_url, {})
util.download_file(uid, '.\\abc.mp4')
