"""
导入markdown文章到cnblogs博客园
post接口：https://i.cnblogs.com/api/posts

post body:
{
  "id": null,
  "postType": 1,
  "accessPermission": 0,
  "title": "nfs服务器之间实现目录共享",
  "url": null,
  "postBody": "* * *\r\n\r\n### title: nfs服务器之间实现目录共享  \r\n date: 2022-11-05 22:41:54  \r\n tags: [nfs，文件共享]  \r\n categories: linux\r\n\r\n在使用airflow的时候，scheduler和worker之间的dag文件需要保持一致，而airflow没有解决这个问题，所以，需要我们自己解决dag文件的同步问题。\r\n\r\n第一个解决方案就是云服务商提供的nas磁盘挂载，使用多台服务器挂载同一个nas盘，实现共享，那么还有其他方式吗？安装软件能解决吗？ok，咱们来介绍一个。\r\n\r\nnfs，网络文件系统，由SUN公司研制的UNIX表示层协议，大家可以放心使用。\r\n\r\n1. 192.168.1.100服务端安装：  \r\n yum install -y nfs-utils rpcbind\r\n \r\n    编辑配置  \r\n vim /etc/exports  \r\n /opt/airflow/dags \\*(rw,sync,insecure,no\\_subtree\\_check,no\\_root\\_squash)  \r\n /opt/airflow/jobs \\*(rw,sync,insecure,no\\_subtree\\_check,no\\_root\\_squash)\r\n \r\n    启动服务：  \r\n service rpcbind start  \r\n service nfs start\r\n \r\n    查看服务器端是否正常加载/etc/exports配置文件  \r\n showmount -e localhost  \r\n \\*-代表允许所有客户端挂载\r\n \r\n    查看注册的端口列表  \r\n rpcinfo -p localhost\r\n2. 192.168.1.101 192.168.1.102客户端安装：  \r\n yum install nfs-utils\r\n \r\n    查看服务端可共享的目录  \r\n showmount -e 192.168.1.100\r\n \r\n    挂载服务端共享目录  \r\n mount 192.168.1.100:/opt/airflow/dags /opt/airflow/dags -o proto=tcp -o nolock  \r\n mount 192.168.1.100:/opt/airflow/jobs /opt/airflow/jobs -o proto=tcp -o nolock\r\n\r\nok，亲测可用，今天就记录到这里吧，没事记录一下日常工作内容。",
  "categoryIds": null,
  "categories": ["nfs"],
  "categoryTree": null,
  "collectionIds": null,
  "inSiteCandidate": false,
  "inSiteHome": false,
  "siteCategoryId": null,
  "blogTeamIds": null,
  "isPublished": false,
  "displayOnHomePage": true,
  "isAllowComments": true,
  "includeInMainSyndication": true,
  "isPinned": false,
  "showBodyWhenPinned": false,
  "isOnlyForRegisterUser": false,
  "isUpdateDateAdded": false,
  "entryName": null,
  "description": "这里介绍nfs不同服务器之间的文件共享",
  "featuredImage": null,
  "tags": [],
  "password": null,
  "datePublished": "2024-11-02T14:09:40.364Z",
  "dateUpdated": null,
  "isMarkdown": true,
  "isDraft": true,
  "autoDesc": null,
  "changePostType": false,
  "blogId": 0,
  "author": null,
  "removeScript": false,
  "clientInfo": null,
  "changeCreatedTime": false,
  "canChangeCreatedTime": false,
  "isContributeToImpressiveBugActivity": false,
  "usingEditorId": 5,
  "sourceUrl": null
}

header:
Content-Type:application/json
Referer:https://i.cnblogs.com/posts/edit
//Sec-Ch-Ua:"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"
Sec-Ch-Ua-Mobile:?0
Sec-Ch-Ua-Platform:"Windows"
X-Xsrf-Token:CfDJ8AOXHS93SCdEnLt5HW8VuxRfW8tiZIgJuarrFh3hgQj3ZUNBmiagne36MKEDixVfkzcraHdz-9s6qkArk83q1FvV9IoRvlZQUanHNTs7Jkg9nq811tKB_XISqhp9huW9SR9wQ8wyWgu9MW6gD7WvcBz3lcEPBUjVfND4-I_BqydI8ULyPJFNlpDh8i_FF94O5A
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
cookie:_ga_3Q0DVSGN10=GS1.1.1727619260.1.1.1727619267.53.0.0; _ga_R55C9JJH2H=GS1.1.1729783573.2.0.1729783573.0.0.0; cto_bundle=5EvJ-F9HMUg0YXA0aGxaOEdBSFc3dExBT2IlMkZGVkVibktsR0Q2YmIybFU5MElwc09ESUowbzNaZjNhT2VGTTlxSVdmUXVQenFiRGxjQVB3M3hoY1NFeFJ2S01KQUVraHR5Q1pwUlhGSzNPS3Q0TklrQ0JDaFZhb1FEZmt6MlhIa05uVk1NZXAyR3pGbERKJTJCVXlpdWZONGhnSCUyRkElM0QlM0Q; cto_bidid=2zwnKl81SmhzNVlIQWRYRkRxbXZyYzAxJTJGU0pnMDBtSVJBSDZESG9GaWNWUEtFZTREY0xZTjl1aWNiQ1pyOVB1NTlyOHFLcGZEbG9vJTJGaGJ0cnZER3NIU0gxUVowaVBLVzQ4WW9VeGk2SmlmZ1JiRW8lM0Q; _ga_7DSFGJNPL4=GS1.1.1730209732.1.0.1730209741.0.0.0; _ga=GA1.1.956593367.1727582784; .Cnblogs.AspNetCore.Cookies=CfDJ8AOXHS93SCdEnLt5HW8VuxQCUbxtbVli5l50_Lb0ttRyyOSAQLwuUs_bbDROVhsI9ucxl_nyMOSImgXW4Q4GxuGeULGZ86A4svSdTsXPFB8ofm54XQVp-Qgtza8CWbc0cyqaOyTHzMcXRNZjEHdrCZZ2-mN0ahHQJ99jvG-6Kl3bMsT41cNs4uppCTTdkWPSDCRbwwdlSkim7pchVuqJaqDGRezfdqgolm3WNEXD_d1wUUD0DEJNvZ7YWkGH8SMFcLC_kdq-ydPL8S1C9nABF0NIRcHvzw0SqoRM4PfXQnAL9uqEHCs48iNybf2TUkYreVV_lcSGAFk62eH8uWdtL3AT7SiSmJtR48gLfVGmoS5FM7YbprpR6tqSfn3m3S-pVrhL1wDoDUYM1jdfW997Rzw5Swrcxwb7YVUdugINGjXcMrYM-nak_0dMLVbFEGyEduGCZbbNvcediHUmAmcqYl-gyfxcjQemWq0I-OfiCSQeDBVH9M2tq7DtzTTRLvWY5hcI96T1Lw94p5qODltOdJOAf9EKlOy3F4uYNI7SUo1Ep4fdn7U6hM9ehywyWvReJOQ7OIOBJcgWAVDhV8k6WsPNXUqeOY9Mrs33WHm6Smxx; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1730216789,1730293578,1730384656,1730551761; HMACCOUNT=8565DD889761288A; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8AOXHS93SCdEnLt5HW8VuxSoBYwSinMZv7eORmYe_1VvPLTg9T-SuvcAFsD-_3qEfta4gEsL0NpM8jn4smqUHV0oZIQ7NoC63L8k5q1TxcpHdEH7WgV9urudTK45QWMhDUM3I-B_P37JnHu0Kxzv8g8; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1730553538; XSRF-TOKEN=CfDJ8AOXHS93SCdEnLt5HW8VuxRfW8tiZIgJuarrFh3hgQj3ZUNBmiagne36MKEDixVfkzcraHdz-9s6qkArk83q1FvV9IoRvlZQUanHNTs7Jkg9nq811tKB_XISqhp9huW9SR9wQ8wyWgu9MW6gD7WvcBz3lcEPBUjVfND4-I_BqydI8ULyPJFNlpDh8i_FF94O5A; _ga_M95P3TTWJZ=GS1.1.1730557108.38.0.1730557108.0.0.0; _ga_C2LFP3RFGH=GS1.1.1730562178.12.1.1730562215.0.0.0
"""
import json

import requests


def main():
    """
    请求
    """
    header = {
        'Content-Type': 'application/json',
        'Referer': 'https://i.cnblogs.com/posts/edit',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'X-Xsrf-Token': 'CfDJ8AOXHS93SCdEnLt5HW8VuxRfW8tiZIgJuarrFh3hgQj3ZUNBmiagne36MKEDixVfkzcraHdz-9s6qkArk83q1FvV9IoRvlZQUanHNTs7Jkg9nq811tKB_XISqhp9huW9SR9wQ8wyWgu9MW6gD7WvcBz3lcEPBUjVfND4-I_BqydI8ULyPJFNlpDh8i_FF94O5A',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': '_ga_3Q0DVSGN10=GS1.1.1727619260.1.1.1727619267.53.0.0; _ga_R55C9JJH2H=GS1.1.1729783573.2.0.1729783573.0.0.0; cto_bundle=5EvJ-F9HMUg0YXA0aGxaOEdBSFc3dExBT2IlMkZGVkVibktsR0Q2YmIybFU5MElwc09ESUowbzNaZjNhT2VGTTlxSVdmUXVQenFiRGxjQVB3M3hoY1NFeFJ2S01KQUVraHR5Q1pwUlhGSzNPS3Q0TklrQ0JDaFZhb1FEZmt6MlhIa05uVk1NZXAyR3pGbERKJTJCVXlpdWZONGhnSCUyRkElM0QlM0Q; cto_bidid=2zwnKl81SmhzNVlIQWRYRkRxbXZyYzAxJTJGU0pnMDBtSVJBSDZESG9GaWNWUEtFZTREY0xZTjl1aWNiQ1pyOVB1NTlyOHFLcGZEbG9vJTJGaGJ0cnZER3NIU0gxUVowaVBLVzQ4WW9VeGk2SmlmZ1JiRW8lM0Q; _ga_7DSFGJNPL4=GS1.1.1730209732.1.0.1730209741.0.0.0; _ga=GA1.1.956593367.1727582784; .Cnblogs.AspNetCore.Cookies=CfDJ8AOXHS93SCdEnLt5HW8VuxQCUbxtbVli5l50_Lb0ttRyyOSAQLwuUs_bbDROVhsI9ucxl_nyMOSImgXW4Q4GxuGeULGZ86A4svSdTsXPFB8ofm54XQVp-Qgtza8CWbc0cyqaOyTHzMcXRNZjEHdrCZZ2-mN0ahHQJ99jvG-6Kl3bMsT41cNs4uppCTTdkWPSDCRbwwdlSkim7pchVuqJaqDGRezfdqgolm3WNEXD_d1wUUD0DEJNvZ7YWkGH8SMFcLC_kdq-ydPL8S1C9nABF0NIRcHvzw0SqoRM4PfXQnAL9uqEHCs48iNybf2TUkYreVV_lcSGAFk62eH8uWdtL3AT7SiSmJtR48gLfVGmoS5FM7YbprpR6tqSfn3m3S-pVrhL1wDoDUYM1jdfW997Rzw5Swrcxwb7YVUdugINGjXcMrYM-nak_0dMLVbFEGyEduGCZbbNvcediHUmAmcqYl-gyfxcjQemWq0I-OfiCSQeDBVH9M2tq7DtzTTRLvWY5hcI96T1Lw94p5qODltOdJOAf9EKlOy3F4uYNI7SUo1Ep4fdn7U6hM9ehywyWvReJOQ7OIOBJcgWAVDhV8k6WsPNXUqeOY9Mrs33WHm6Smxx; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1730216789,1730293578,1730384656,1730551761; HMACCOUNT=8565DD889761288A; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8AOXHS93SCdEnLt5HW8VuxSoBYwSinMZv7eORmYe_1VvPLTg9T-SuvcAFsD-_3qEfta4gEsL0NpM8jn4smqUHV0oZIQ7NoC63L8k5q1TxcpHdEH7WgV9urudTK45QWMhDUM3I-B_P37JnHu0Kxzv8g8; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1730553538; XSRF-TOKEN=CfDJ8AOXHS93SCdEnLt5HW8VuxRfW8tiZIgJuarrFh3hgQj3ZUNBmiagne36MKEDixVfkzcraHdz-9s6qkArk83q1FvV9IoRvlZQUanHNTs7Jkg9nq811tKB_XISqhp9huW9SR9wQ8wyWgu9MW6gD7WvcBz3lcEPBUjVfND4-I_BqydI8ULyPJFNlpDh8i_FF94O5A; _ga_M95P3TTWJZ=GS1.1.1730557108.38.0.1730557108.0.0.0; _ga_C2LFP3RFGH=GS1.1.1730562178.12.1.1730562215.0.0.0'
    }
    cnblog_url = 'https://i.cnblogs.com/api/posts'

    data = {
        "postType": 1,
        "accessPermission": 0,
        "title": "nfs服务器之间实现目录共享11",
        "postBody": "* * *\r\n\r\n### title: nfs服务器之间实现目录共享  \r\n date: 2022-11-05 22:41:54  \r\n tags: [nfs，文件共享]  \r\n categories: linux\r\n\r\n在使用airflow的时候，scheduler和worker之间的dag文件需要保持一致，而airflow没有解决这个问题，所以，需要我们自己解决dag文件的同步问题。\r\n\r\n第一个解决方案就是云服务商提供的nas磁盘挂载，使用多台服务器挂载同一个nas盘，实现共享，那么还有其他方式吗？安装软件能解决吗？ok，咱们来介绍一个。\r\n\r\nnfs，网络文件系统，由SUN公司研制的UNIX表示层协议，大家可以放心使用。\r\n\r\n1. 192.168.1.100服务端安装：  \r\n yum install -y nfs-utils rpcbind\r\n \r\n    编辑配置  \r\n vim /etc/exports  \r\n /opt/airflow/dags \\*(rw,sync,insecure,no\\_subtree\\_check,no\\_root\\_squash)  \r\n /opt/airflow/jobs \\*(rw,sync,insecure,no\\_subtree\\_check,no\\_root\\_squash)\r\n \r\n    启动服务：  \r\n service rpcbind start  \r\n service nfs start\r\n \r\n    查看服务器端是否正常加载/etc/exports配置文件  \r\n showmount -e localhost  \r\n \\*-代表允许所有客户端挂载\r\n \r\n    查看注册的端口列表  \r\n rpcinfo -p localhost\r\n2. 192.168.1.101 192.168.1.102客户端安装：  \r\n yum install nfs-utils\r\n \r\n    查看服务端可共享的目录  \r\n showmount -e 192.168.1.100\r\n \r\n    挂载服务端共享目录  \r\n mount 192.168.1.100:/opt/airflow/dags /opt/airflow/dags -o proto=tcp -o nolock  \r\n mount 192.168.1.100:/opt/airflow/jobs /opt/airflow/jobs -o proto=tcp -o nolock\r\n\r\nok，亲测可用，今天就记录到这里吧，没事记录一下日常工作内容。",
        "categories": ["nfs"],
        "inSiteCandidate": False,
        "inSiteHome": False,
        "isPublished": False,
        "displayOnHomePage": True,
        "isAllowComments": True,
        "includeInMainSyndication": True,
        "isPinned": False,
        "showBodyWhenPinned": False,
        "isOnlyForRegisterUser": False,
        "isUpdateDateAdded": False,
        "description": "这里介绍nfs不同服务器之间的文件共享",
        "tags": [],
        "datePublished": "2024-11-02T14:09:40.364Z",
        "isMarkdown": True,
        "isDraft": True,
        "changePostType": False,
        "blogId": 0,
        "author": "chenzuoli",
        "removeScript": False,
        "changeCreatedTime": False,
        "canChangeCreatedTime": False,
        "isContributeToImpressiveBugActivity": False,
        "usingEditorId": 5,
    }
    response = requests.post(cnblog_url, headers=header, data=json.dumps(data))
    print(response.status_code, response.json())


if __name__ == '__main__':
    main()
