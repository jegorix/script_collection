
def get_float(promt):
    while True:
        try:
            value = float(input(promt))
            return value
        except ValueError:
            print("Error! Type number!")
    

def get_positive_float(promt):
    while True:
        value = get_float(promt)
        if value > 0:
            return value
        print("Incorrect! Weight should be greater than zero!")
            

def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
    