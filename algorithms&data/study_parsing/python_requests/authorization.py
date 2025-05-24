from requests import Session
from bs4 import BeautifulSoup
from data import authorization_url as main_url, USER_AGENT, authorization_url_login as url_login, STATIC_PATH as path
import json

headers = {
    "user_agent": USER_AGENT
}



workflow = Session()
workflow.get(main_url, headers=headers)
response = workflow.get(url_login, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
csrf_token = soup.find("form").find("input").get("value")

data_login = {
    "csrf_token": csrf_token,
    "username": "NoName",
    "password": "password1234"
}

result_login = workflow.post(url_login, headers=headers, data=data_login, allow_redirects=True)
logged_soup = BeautifulSoup(result_login.text, 'lxml')
logout = logged_soup.find("div", class_ = "col-md-4").find("a").text

if logout == "Logout":
    print("You are successfully logged in")
else:
    print("ERROR! You are not logged in")


def get_quote(counter):
    while logout:
        counter += 1
        response_page = workflow.get(main_url + f"page/{counter}/")
        page_soup = BeautifulSoup(response_page.text, 'lxml')
        block_cyt = page_soup.find_all("div", class_ = "quote")
        for block in block_cyt:
            text = block.find("span", class_ = "text").text
            author = block.find("small", class_ = "author").text
            author_links = block.find_all("a", class_ = None) 
            for link in author_links:
                if link.text == '(Goodreads page)':
                    author_link = link.get("href")
            # print('\n' + f"Quote: {text}", f"By {author}", f"Authors page: {author_link}" + '\n', sep='\n')
            data = (text, author, author_link)
            yield data


    
def make_json():
    counter = 0
    number = 1
    with open(path + 'quotes.json', "w", encoding="utf-8") as file:
        for tup in get_quote(counter):
            data = {
                f'name_{number}': tup[0],
                f'author_{number}': tup[1],
                f'author_page_{number}': tup[2],
            }
            json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Quote-{number} successfully added...")
            number += 1
        




if __name__ == '__main__':
    make_json()