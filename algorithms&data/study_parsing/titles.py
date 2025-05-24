import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import json 


# PATH = '/Users/macbook/PycharmProjects/scripts_edu/algorithms&data/study_parsing/static/proxy_2.json'
# with open(PATH, mode="r") as file:
#     parsed = json.load(file)
    
# proxy_list = []
# for adress in parsed:
#     link = f"http://{adress['ip']}:{adress['port']}"
#     proxy_list.append(link)

# urls = [
#     'https://www.python.org',
#     'https://www.wikipedia.org',
#     'https://www.github.com',
#     'https://www.stackoverflow.com'
# ]


# if len(proxy_list) < len(urls):
#     raise ValueError("Not enough proxies: must be at least as many as URLs!")

# def fetch_title(task):
#     url, proxy_adress = task
#     proxy = {'http': proxy_adress, 'https': proxy_adress}
#     try:
#         ip_response = requests.get('http://httpbin.org/ip', proxies=proxy, timeout=5)
#         ip = ip_response.json().get('origin')
#         print(ip)
#     except Exception as e:
#         print(e)
#         print('ERROR')

# links = list(zip(urls, proxy_list))
# fetch_title(task=('https://www.python.org', 'http://67.43.236.19:26025'))


url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
response = requests.get(url)
data = response.json()
proxy_list = []

for item in data['data']:
    if 'http' in item.get('protocols', []):
        proxy_list.append(f"http://{item['ip']}:{item['port']}")

def is_proxy_alive(proxy_str):
    proxies = {
        'http': proxy_str,
        'https': proxy_str
    }

    try:
        r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if r.status_code == 200:
            print(f"✅ Рабочий: {proxy_str}")
            return True
    except Exception as e:
        print(f"❌ Не работает: {proxy_str} ({e})")
    return False


working_proxies = [proxy for proxy in proxy_list if is_proxy_alive(proxy)]


