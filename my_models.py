import os
import json
import requests
from datetime import date
from my_globals import LATITUDE, LONGITUDE, TIMEZONE, CACHE_FILE

class Weather:
    def __init__(self, user_date):
        self.start_date = user_date
        #self.end_date = str(date.fromisoformat(user_date).replace(day = date.fromisoformat(user_date).day + 1))
        self.end_date = user_date
    
    def get_weather(self):
        api_call = "https://api.open-meteo.com/v1/forecast?latitude=" + LATITUDE + "&longitude=" + LONGITUDE + "&hourly=rain&daily=rain_sum&timezone=" + TIMEZONE + "&start_date=" + self.start_date + "&end_date=" + self.end_date
        req = requests.get(api_call)
        if req.status_code in [200]:
            self.save_date_to_cache(req.json())
            return req.json()
        else:
            print(f"Błąd łączenia z serverem, status {req.status_code}")
            
    def weather_cache_file_exists(self):
        if os.path.exists(CACHE_FILE):
            return True
        return False

    def save_date_to_cache(self, weather_req):
        with open(CACHE_FILE, mode = 'a') as f:
            f.write(f"date_log: {self.start_date}\n")
            json.dump(weather_req, f)
            f.write("\n")
    
    def check_data_from_cache(self):
        # ma zwrócić true jeśli dana znajduje się w pliku
        pass
    
    def read_data_from_cache(self):
        # dokonczyc odczyt z pliku daty jeśli już jest (dodać warunke check_data_from_cache)
        if self.weather_cache_file_exists() == True:
            with open(CACHE_FILE, mode = 'r') as f:
                cache = f.readlines()
        return cache
        
    def will_it_rain(self):
        weather = self.get_weather()
        if weather['daily']['rain_sum'][0] == 0.0:
            print(f'Nie będzie padać...')
        elif weather['daily']['rain_sum'][0] > 0.0:
            print(f'Będzie padać...')
        elif weather['daily']['rain_sum'][0] < 0.0 or weather['daily']['rain_sum'][0] == None:
            print(f'Nie wiem czy będzie padać, szklaną kulę rozbiłem...')