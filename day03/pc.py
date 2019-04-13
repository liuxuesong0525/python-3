import requests
# url = 'http://10.56.27.6:8080/web/index.html'
# response = requests.get(url)
# if response.status_code == 200:
#     print(response.text)

# url = 'http://10.56.27.6:8080/web/index.html'
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# response = requests.get(url,headers = headers)
# if response.status_code == 200:
#     print(response.text)


# url = 'http://10.56.27.6:8080/web/a.jsp'
# kw = {'name':'zhangshang','age':33}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# response = requests.post(url,headers = headers,params = kw)
# if response.status_code == 200:
#     print(response.text)


url = 'http://www.baidu.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
proxies = {"http":"http://125.67.25.83:48373"}
response = requests.post(url,headers = headers,proxies = proxies)
if response.status_code == 200:
    print(response.text)





