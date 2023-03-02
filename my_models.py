import requests
from datetime import date
from my_globals import API_URL, LATITUDE, LONGITUDE, TIMEZONE
class Weather:
    def __init__(self, user_date):
        self.start_date = user_date
        #self.end_date = str(date.fromisoformat(user_date).replace(day = date.fromisoformat(user_date).day + 1))
        self.end_date = user_date
    
    def get_weather(self):
        api_call = "https://api.open-meteo.com/v1/forecast?latitude=" + LATITUDE + "&longitude=" + LONGITUDE + "&hourly=rain&daily=rain_sum&timezone=" + TIMEZONE + "&start_date=" + self.start_date + "&end_date=" + self.end_date
        req = requests.get(api_call)
        if req.status_code in [200]:
            return req.json()
        else:
            print(f"Błąd łączenia z serverem, status {req.status_code}")
    
    def will_it_rain(self):
        weather = self.get_weather()
        if weather['daily']['rain_sum'][0] == 0.0:
            print(f'Nie będzie padać...')
            break
        elif weather['daily']['rain_sum'][0] > 0.0:
            print(f'Będzie padać...')
            break
        elif weather['daily']['rain_sum'][0] < 0.0 or weather['daily']['rain_sum'][0] == None:
            print(f'Nie wiem czy będzie padać, szklaną kulę rozbiłem...')
            break
            
        