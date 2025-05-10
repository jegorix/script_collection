import requests
from bs4 import BeautifulSoup
import fake_useragent



class RateExchange:

    main_link = "https://myfin.by/bank/belarusbank/department/10569-minsk-ul-yanki-brylya-30/courses"

    @staticmethod
    def get_rate_array():
        user_agent = fake_useragent.UserAgent().random
        headers = {
            'user_agent': user_agent
        }

        response = requests.get(url = RateExchange.main_link, headers=headers).text
        soup = BeautifulSoup(response, 'lxml')

        rates_blocks = soup.find("div", class_ = "expandable-exchange-rates").find_all("div", class_ = "expandable-exchange-rates__body-item")

        return [block.text for block in rates_blocks[:]]


    @staticmethod
    def create_rates_dict(block_text):
        rate_dict = {}
        tens = ['10', '100', '1000']

        for line in block_text:
            line = line.split()
            for num in line:
                if num in tens:
                    line[0] = f"{line[0]}({num})"
                    line.remove(num)

            rate_dict[line[0]] = [line[1], line[2]]
        return rate_dict


    def create_dict(self):
        rates_blocks_text = RateExchange.get_rate_array()
        rate_dict = RateExchange.create_rates_dict(rates_blocks_text)
        return rate_dict
    
    def show_rates(self):
        for (k,v) in self.create_dict().items():
            result = f"\n{k}:\nSELL: {v[0]}\nBUY: {v[1]}\n"
            print(result)

    def show_names(self):

        rates_dict = self.create_dict()
        for i, k in enumerate(rates_dict.keys(), start = 1):
            print(f"{i}.{k}")

      

    def get_rate(self, choice):
        rates_dict = self.create_dict()
        choice_dict = {i+1: (key, value) for i, (key, value) in enumerate(rates_dict.items())}
        return choice_dict.get(choice, "Uknown choice")


        

    def sum_calculate(self, amount, rate_tuple):
        sell_buy_dict = {
            1: f"SELL '{rate_tuple[0]}'",
            2: f"BUY '{rate_tuple[0]}'"
        }
        sell_price, buy_price = float(rate_tuple[1][0]), float(rate_tuple[1][1])

        for k,v in sell_buy_dict.items():
            print(f"{k}.{v}")

        operation_choice = float(input("Select type of transfer: "))
        print(f"Selected: {sell_buy_dict.get(operation_choice, "Uknown choice")}")
        
        match operation_choice:
            case 1:
                return f"\nResult(sell) = {round(amount / sell_price, 4)} {rate_tuple[0]}"
            case 2:
                return f"\nResult(buy) = {round(amount / buy_price, 4)} {rate_tuple[0]}"


        return "Unexpected error"
        
        

def main():
    rates = RateExchange()
    print("\nSelect currency:")
    rates.show_names() #fix
    choice = int(input("\nEnter the ordinal number of the currency: "))
    rate = rates.get_rate(choice)
    print(f"\nSelected currency: {rate}")
    user_amount = int(input("\nEnter the desired amount in BYN's: "))
    result = rates.sum_calculate(user_amount, rate)
    print(result)
    



if __name__ == "__main__":
    main()
    



