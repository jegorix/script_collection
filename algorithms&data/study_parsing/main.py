import requests
from bs4 import BeautifulSoup
import fake_useragent

# link = "https://icanhazip.com"
# response = requests.get(link).text
# response_2 = requests.get(link).content
# # print(response.status_code)
# print(response)
# print(response_2)


# apple_link = "https://www.ubuy.ie/en/product/3TOPWLWVA-red-delicious-apples-each?ref=hm-google-redirect"
# response_3 = requests.get(apple_link).content
# print(response_3)

# browser_info_link = "https://browser-info.ru"
# browser_info_response = requests.get(browser_info_link).text
#
# file = "static/index.html"
# with open(file, "w", encoding="utf-8") as f:
#     f.write(browser_info_response)






user = fake_useragent.UserAgent().random
header = {"user-agent": user}


link = "https://browser-info.ru/"
response = requests.get(link, headers=header).text
soup = BeautifulSoup(response, "lxml")
# block = soup.find_all("div")

#blocks
block = soup.find("div", id="tool_padding")
footer = soup.find("div", id="footer")

#check javascript
check_js = block.find("div", id="javascript_check")
result_js = f"Javascript: {check_js.find_all("span")[1].text}"

#check cookie
check_cookie = block.find("div", id="cookie_check")
result_cookie = f"Cookie: {check_cookie.find_all("span")[1].text}"

#check flash
check_flash = block.find("div", id="flash_version")
result_flash = f"Flash: {check_flash.find_all("span")[1].text}"

#user_agent
user_agent = block.find("div", id="user_agent").text
# result_user_agent = f"User-Agent: {user_agent}"

# get link-copyright
check_copyright= footer.find("div", id="site_copyright")
result_copyright_link = f"Copyright-link: {check_copyright.find("a").get("href")}"




print("\n",result_flash)
print(result_js)
print(result_cookie)
print(user_agent)
print(result_copyright_link)














