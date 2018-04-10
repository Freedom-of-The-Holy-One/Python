r=requests.get(url,params,**kwargs)

url:获取页面的url

params：url中的额外参数，字典或字节流格式，可选

**kwargs：12个控制访问的参数

Response对象的属性

|         属性          |              说明               |
| :-----------------: | :---------------------------: |
|    r.status_code    | HTTP请求的返回状态，200表示连接成功，404表示失败 |
|       r.text        |  HTTP响应内容的字符串形式。即：url对应的页面内容  |
|     r.encoding      |   从HTTP header中猜测的响应内容编码方式    |
| r.apparent_encoding |   从内容中分析出的响应内容的编码方式(备选编码方式)   |
|      r.content      |        HTTP响应内容的二进制形式         |

--r.status_code分两步

r.encoding('utf-8')--->r.text

r.eocoding:如果header中不存在charset,则认为编码为ISO-8859-1

R.APPAERNT_eocoding:根据网页内容分析出的编码方式

r.encoding：根据头部信息获取到的编码方式



Requests库异常：

|             异常              |               说明               |
| :-------------------------: | :----------------------------: |
|  requests.ConnectionError   |    网络连接错误异常，如DNS查询失败、拒绝连接等     |
|     requests.HTTPError      |            HTTP错误异常            |
|    requests.URLRequired     |            URL缺失异常             |
|  requests.TooManyRedirects  |       超过最大重定向次数，产生重定向异常        |
|   requests.ConnectTimeout   |          连接远程服务器超时异常           |
|      requests.Timeout       |         请求URL超时，产生超时异常         |
| response.raise_for_status() | 如果不是200，产生异常requests.HTTPError |



通用代码框架

```
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        //如果不是200，产生异常HTTPError
        r.raise_for_status()
        r,encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
```
------

##### 正则表达式

