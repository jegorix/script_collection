
from exceptions import CreditCardPaymentError, CryptoPaymentError


class Validators:
    
    @staticmethod
    def rmchar(text: str, char: str = " ") -> str:
        return text.replace(char, "")
    
    @classmethod
    def valid_card_number(cls, value: str) -> bool | None:
        try:
            card_number = int(cls.rmchar(value))
            if len(str(card_number)) != 16:
                print("Card length error")
                raise CreditCardPaymentError
            
        except Exception:
            print("Not digit value")
            raise CreditCardPaymentError
        
        return True
        
        
    @classmethod
    def valid_wallet_adress(cls, value: str) -> bool | None:
        if not value.startswith("0x"):
            print("Wrong wallet adress")
            raise CryptoPaymentError
        
        return True


if __name__ == "__main__":
    print("SUCCESS")