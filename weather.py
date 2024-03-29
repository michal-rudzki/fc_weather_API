import json
from datetime import date

from my_models import *
from my_globals import TIMEZONE

def main():

    while True:
        print(f"Podaj date w formacie YYYY-mm-dd, np. {date.today()}")
        user_input = input()
        if not user_input:
            user_input = date.isoformat(date.today())
            print(user_input)
        elif user_input in ['q', 'quit']:
            break
        
        weather = Weather(user_input)
        weather.will_it_rain()
        print(weather.items())
        for d in weather:
            print(d)
        
        
if __name__ == "__main__":
    main()