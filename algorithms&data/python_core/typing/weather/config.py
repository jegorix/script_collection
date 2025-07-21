
USE_ROUNDED_COORDS = True

 
OPENWEATHER_API = "7549b3ff11a7b2f3cd25b56d21c83c6a" 
 
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)