import requests
url = 'http://httpbin.org/get'
# proxy = requests.get('http://127.0.0.1:5000/random').text
proxy = '39.137.69.7:80'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
res = requests.get(url=url,proxies=proxies)
print(res.text)