import logging
import os
import sys
import time

import requests

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


class HttpRequestUtil:
    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    def get(self, endpoint, params=None):
        """
        发送GET请求
        :param endpoint: 路由地址（不包括基本URL）
        :param params: 查询参数（可选）
        :param headers: HTTP头部（可选）
        :return: 响应对象
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=self.header)
        response.raise_for_status()  # 如果响应状态码不是200，则抛出HTTPError异常
        return response

    def post(self, endpoint, data=None, json=None):
        """
        发送POST请求
        :param endpoint: 路由地址（不包括基本URL）
        :param data: 表单数据（可选）
        :param json: JSON数据（可选）
        :param headers: HTTP头部（可选）
        :return: 响应对象
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data, json=json, headers=self.header)
        response.raise_for_status()  # 如果响应状态码不是200，则抛出HTTPError异常
        return response

    def download_image_file(self, image_url, file_path):
        """
        下载星球图片
        :param image_url:
        :param file_path:
        :return:
        """
        time.sleep(2)
        response = requests.get(image_url, stream=True, headers=self.header)

        # 确保请求成功
        response.raise_for_status()

        # 打开一个文件用于写入
        with open(file_path, 'wb') as file:
            # 迭代响应的内容
            for chunk in response.iter_content(chunk_size=8192):
                # 如果chunk存在，写入文件
                if chunk:
                    file.write(chunk)

    def download_file(self, uid, file_path):
        """
        下载星球文件
        :param url:
        :param file_path:
        :return:
        """
        download_file_url = self.base_url + uid
        print("downlaod file url: " + download_file_url)
        self.save_download_urls(download_file_url, file_path)
        file_response = requests.get(download_file_url, stream=True, headers=self.header)
        # 打开一个文件用于写入
        with open(file_path, 'wb') as file:
            # 迭代响应的内容
            for chunk in file_response.iter_content(chunk_size=8192):
                # 如果chunk存在，写入文件
                if chunk:
                    file.write(chunk)

    def save_download_urls(self, download_url: str, file_path: str):
        """
        保存下载链接
        :param download_url:
        :param file_path:
        :return:
        """
        dirname = os.path.dirname(file_path)
        download_urls_file_path = os.path.join(dirname, 'download_urls.txt')
        with open(download_urls_file_path, 'a') as f:
            f.write(download_url + '\n')
            f.flush()

    def get_download_url(self, url):
        """
        下载星球文件
        :param url:
        :param file_path:
        :return:
        """
        time.sleep(2)
        # 发送GET请求
        response = requests.get(url, headers=self.header)

        # 确保请求成功
        response.raise_for_status()

        if response.status_code == 200:
            print(response.json())
            download_file_url = response.json()['resp_data']['download_url']
            print("downlaod file url: " + download_file_url)
            return download_file_url
        else:
            raise Exception('error request download url')


if __name__ == "__main__":
    # 使用示例
    headers = {"Authorization": "Bearer your_token_here"}
    http_util = HttpRequestUtil("http://example.com/api", header=headers)

    # 发送GET请求
    response_get = http_util.get("/users", params={"id": 123})
    print(response_get.json())

    # 发送POST请求（表单数据）
    response_post_form = http_util.post("/login", data={"username": "user", "password": "pass"})
    print(response_post_form.json())

    # 发送POST请求（JSON数据）
    response_post_json = http_util.post("/items", json={"name": "New Item", "price": 100})
    print(response_post_json.json())
