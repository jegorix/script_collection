import requests
from data import API_TOKEN, KELVIN, MAIN_URL, USER_AGENT, IMAGE_PATH
from rich import print
from bs4 import BeautifulSoup
from time import sleep



headers = {
    "user_agent": USER_AGENT
}


def download(url):
    resp = requests.get(url, stream=True)
    with open(f"{IMAGE_PATH}" + url.split('/')[-1], "wb") as file:
        for value in resp.iter_content(1024*1024):
            file.write(value)



 
def get_card():
    for page_value in range(1,7):
        url_club = f"https://scrapingclub.com/exercise/list_basic/?page={page_value}"
        

        response = requests.get(url_club, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        datasets = soup.find_all("div", class_ = "w-full rounded border")

        for data in datasets:
            card_url = MAIN_URL + data.find("a").get("href")
            yield card_url

# generator( yield usage )


def make_collection():
    for card_link in get_card():
        response_card = requests.get(card_link, headers=headers)
        # sleep(2) time-consuming
        soup_card = BeautifulSoup(response_card.text, 'lxml')

        datasets_cards = soup_card.find("div", class_ = 'my-8 w-full rounded border')

        name = datasets_cards.find("h3", class_ = "card-title").text
        price = datasets_cards.find("h4", class_ = "my-4 card-price").text
        description = datasets_cards.find("p", class_ = "card-description").text
        url_img = MAIN_URL + datasets_cards.find("img", class_ = "card-img-top").get("src")
        # result = f"\nProduct name: {name}\nPrice: {price}\nDescription: {description}\nImage url: {url_img}\n\n"
        data = (name, price, description, url_img)
        download(url_img)
        yield data









# def main():
#     params = {
#         "q": "Paris",
#         "appid": API_TOKEN,
#         "units": "metric"
#     }


#     response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
#     response_dict = response.json()
#     result = f'''
#     Status: {response_dict['weather'][0]['main']}\n
#     Temperature: {response_dict['main']['temp']}\n
#     Humidity: {round(response_dict['main']['humidity'])}%\n
#     '''
#     print(result)
#     print(response.headers)





#     data = {
#         "custname": "Fred",
#         "custtel": "111111",
#         "custemail": "nptspam@gmail.com",
#         "size": "medium",
#         "topping": "bacon",
#         "comments": "CEO"
#     }


    
#     headers = {
#     "Accept": "application/json",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "ru",
#     "Host": "httpbin.org",
#     "Referer": "https://httpbin.org/",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
#     "X-Amzn-Trace-Id": "Root=1-6830d045-5d6d6f3f17a50a2863f4d776"
#   }
    
#     session = requests.Session()
#     token = session.get("https://httpbin.org/forms/post")

#     response_httpbin = session.post("https://httpbin.org/post", headers=headers, data=data, allow_redirects=True)
#     print(response_httpbin.text)


# if __name__ == "__main__":
#     main() 




