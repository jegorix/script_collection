
def parse_number(value: str) -> int | float | None:
    
    try:
        return int(value)
    except ValueError:
        
        try:
            return float(value)
        except ValueError:
            return None
            
    