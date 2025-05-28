
def get_float(promt):
    while True:
        try:
            value = float(input(promt))
            return value
        except ValueError:
            print("Error! Type number!")
    

def get_positive_float(promt):
    while True:
        value = float(input(promt))
        if value > 0:
            return value
        print("Incorrect! Weight should be greater than zero!")
            
            