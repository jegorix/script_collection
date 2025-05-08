import requests
from bs4 import BeautifulSoup
import fake_useragent

image_number = 1
page_number = 1

path_img = "/Users/macbook/Desktop/bbc_image"
main_link = "https://pressa.tv"

for page in range(1, 5):

    if page_number > 1:
        link = f"https://pressa.tv/comics/page/{page_number}/"
    else:
        link = "https://pressa.tv/comics/"

    user_agent = fake_useragent.UserAgent().random
    headers = {'user-agent': user_agent}

    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')

    block_memes = soup.find("div", id = "dle-content")



    data_image_blocks = block_memes.find_all("div", attrs={"class": "th"})
    image_blocks = [block.find("div", class_ = None).find("img")["data-src"] for block in data_image_blocks]

    for image_link in image_blocks:
        full_image_link = f"{main_link}{image_link}"
        image_bytes = requests.get(full_image_link, headers=headers).content

        with open(f"{path_img}/{image_number}.jpg", 'wb') as file:
            file.write(image_bytes)

        print(f"Meme image №{image_number} - successfully downloaded!")
        image_number += 1

    print(f"\nMemes from page №{page_number} - successfully downloaded!\n")
    page_number += 1


print("Meme images was successfully downloaded!")










