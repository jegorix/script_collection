import requests
from bs4 import BeautifulSoup
import fake_useragent

#session, authorization, cookie
#login: jegorix
#password: egor12211221


def main():
        session = requests.Session()
        # link = "http://forum.watch.ru/login.php?do=login&r=57984"
        # link = "https://automationexercise.com/login"
        # link = "https://practice.expandtesting.com/login"
        # link = "https://the-internet.herokuapp.com/login"
        link = "https://the-internet.herokuapp.com/authenticate"
        profile_link = "https://the-internet.herokuapp.com/secure"

        user = fake_useragent.UserAgent().random

        header = {
            'user-agent': user,
        }




        data = {
            "username": "tomsmith",
            "password": "SuperSecretPassword!"
        }




        #save & load cookies
        cookies_dict = [
            {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
            for key in session.cookies
        ]

        session2 = requests.Session()
        for cookie in cookies_dict:
            session2.cookies.set(**cookie)



        response = session.post(link, data=data, headers=header)

        print(f"Status code: {response.status_code}")
        print(f"URL: {response.url}")


        # profile_link = response.url
        def parse_info(profile_link):
            profile_response = session2.get(profile_link, headers=header).text
            soup = BeautifulSoup(profile_response, "lxml")
            block = soup.find("div", attrs={"class": "example"})
            check_area = block.find_all("h4", attrs={"class": "subheader"})

            for h in check_area:
                print(f"SECURE TEXT: {h.get_text(strip=True)}")


        if "Welcome" in response.text or "Logout" in response.text:
            print("successful login")
            parse_info(response.url)
        else:
            print("unsuccessful login")




if __name__ == "__main__":
    main()