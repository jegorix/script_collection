from abc import ABC, abstractmethod
from typing import Dict, Any, Callable, ParamSpec, TypeVar
from validators import Validators



P = ParamSpec("P")
T = TypeVar("T")






def validate_payment(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        self = args[0]
        
        if isinstance(self, CreditCardPayment):
            Validators.valid_card_number(self._card_number)
        
        elif isinstance(self, CryptoPayment):
            Validators.valid_wallet_adress(self._wallet_adress)
            
        return func(*args, **kwargs)
    return wrapper
    








class Payment(ABC):
    def __init__(self, amount: float, currency: str, name: str) -> None:
        self._amount = amount
        self._currency = currency
        self._name = name
        
        
    @abstractmethod
    def process(self) -> Dict[str, Any]:
        """Обработать платеж и вернуть статус"""
        pass
    
    
class CreditCardPayment(Payment):
    def __init__(self, amount: float,
                 currency: str,
                 name: str,
                 card_number: str,
                 cvv: int,
                 expiry: str
                 ) -> None:
        
        self._card_number = card_number
        self._cvv = cvv
        self._expiry = expiry
        super().__init__(amount, currency, name)
        
        
    @validate_payment
    def process(self) -> Dict[str, Any]:
        return {"status": "success", "method": "credit card"}
    
    
    def __repr__(self) -> str:
        data = f"""
        Name: {self._name}
        Amount: {self._amount} {self._currency}
        Card number: {self._card_number}
        CVV: {self._cvv}
        Expiry: {self._expiry}
        """
        return data



class CryptoPayment(Payment):
    def __init__(self,
                 amount: float,
                 currency: str,
                 wallet_adress: str,
                 name: str
                 ) -> None:
        
        self._wallet_adress = wallet_adress
        super().__init__(amount, currency, name)
        
        
    @validate_payment
    def process(self) -> Dict[str, Any]:
        return {"status": "success", "method": "crypto"}
    
    def __repr__(self) -> str:
        data = f"""
        Name: {self._name}
        Amount: {self._amount} {self._currency}
        Wallet adress: {self._wallet_adress}
        """
        return data
    
    
    
    

    
    
    
if __name__ == "__main__":
    card_1 = CreditCardPayment(amount=23.23,
                           currency="USD",
                           name="Jane",
                           card_number="2323 2323 2323 2323",
                           cvv=499,
                           expiry="08/28")
    print(card_1)