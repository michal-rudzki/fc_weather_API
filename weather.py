import json
from datetime import date

from my_models import *
from my_globals import TIMEZONE

def main():

    while True:
        print(f"Podaj date w formacie YYYY-mm-dd, np. {date.today()}")
        user_input = input()
        if not user_input:
            user_input = date.today()
            print(f"Przyjmuje date: {user_input.replace(day = user_input.day + 1)}")
            break
        
        weather = Weather(user_input)
        weather.will_it_rain()
        
        

if __name__ == "__main__":
    main()