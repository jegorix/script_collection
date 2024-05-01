import requests
from bs4 import BeautifulSoup
import fake_useragent
from urllib.parse import quote, urljoin
import os

image_number = 1
path_img = "/Users/macbook/Desktop/image"
main_link = "https://1drugni.pukhovichi-asveta.gov.by"

link = "https://1drugni.pukhovichi-asveta.gov.by/%D0%BE%D0%B1-%D1%83%D1%87%D1%80%D0%B5%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B8/%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B8%D0%B2"
user = fake_useragent.UserAgent().random
header = {"user-agent": user}

response = requests.get(link, headers=header).text
soup = BeautifulSoup(response,'lxml')
block_images = soup.find("div", attrs={"class": "col-sm-8 col-lg-9 article"})
images_links = block_images.find_all("div", class_="preview col-sm-2")


names_blocks = block_images.find_all("div", class_="content")
names = [name.find("h3").text for name in names_blocks]

result_names = names[29:-2:]
result_names.insert(0, names[23])



for i, image_link in enumerate(images_links):

    relative_img_url = image_link.find("img")["src"]
    full_img_url = f"{main_link}/{relative_img_url}"

    # folder, filename = os.path.split(relative_img_url)
    # encoded_url = f"{folder}/{quote(filename)}"
    #
    # full_img_url = urljoin(main_link, encoded_url)
    # print(full_img_url)

    #download image
    image_bytes = requests.get(full_img_url, headers=header).content

    # with open(f"{path_img}/t_{image_number}.jpg", "wb") as file:
    with open(f"{path_img}/{result_names[i]}.jpg", "wb") as file:
        file.write(image_bytes)

    image_number += 1
    print(f"Image №{image_number} successfully downloaded!")




