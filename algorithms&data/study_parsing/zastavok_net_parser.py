import requests
from bs4 import BeautifulSoup
import fake_useragent

storage_number = 1
image_number = 1
# path_img = f"static/image"
path_img = f"/Users/macbook/Desktop/image"

link = f"https://zastavok.net"


user = fake_useragent.UserAgent().random
header = {'user-agent': user}


response = requests.get(f"{link}/{storage_number}/", headers=header).text
soup = BeautifulSoup(response, 'lxml')
photo_block = soup.find("div", attrs={"class": "block-photo"})
all_image = photo_block.find_all("div", attrs={"class": "short_full"})

for image in all_image:
    res = image.find("a").get("href")
    # download_image_link = f"{link}/{res}"
    download_storage = requests.get(f"{link}/{res}").text
    download_soup = BeautifulSoup(download_storage, 'lxml')
    download_block = download_soup.find("div", attrs={"class":"image_data"}).find("div", class_="block_down")
    result_link = download_block.find("div").find("a").get("href")

    #download image
    image_bytes = requests.get(f"{link}/{result_link}").content

    with open(f"{path_img}/{image_number}.jpg", "wb") as file:
        file.write(image_bytes)

    image_number += 1
    print(f"Image №{image_number} successfully downloaded!")


print("Finished!")

