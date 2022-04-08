from faker import Faker
import datetime
import random
import json
import random
import faker
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

start_date = "2017-08-01"

cities = [
    {
        "city": "Sydney",
        "creation_date": "2017-09-25"
    },
    {
        "city": "Melbourne",
        "creation_date": "2019-02-14"
    },
    {
        "city": "Brisbane",
        "creation_date": "2020-02-15"
    },
    {
        "city": "Perth",
        "creation_date": "2022-01-10"
    },
]


def stream_write_json(json_object):
    with open('outputs/meetup_member.json','a') as f:
        f.write(json.dumps(json_object))
        f.write("\u000a")

def get_member():
    x = 1
    while x < 2200:
        for city in cities:
            date_format = '%Y-%m-%d'
            dtObj = datetime.strptime(start_date, date_format)
            future_date = dtObj + relativedelta(days=x)
            # print(f'city: {city}')
            city_name = city['city']
            creation_date = datetime.strptime(city['creation_date'], date_format)
            if future_date >= creation_date:
                meetup_date = f'{future_date.year}-{future_date.month}-{day_date}'
                print(f'{city_name} is on {meetup_date}')
                result = generate_meetup_events(city_name, 'asdf', meetup_date)
                stream_write_json(result)
        x += 1

def generate_member(city, company, date):
    fake = Faker('en_AU')

    # a Python object (dict):
    member_object = {
        "city": city,
        "signup_date": date,
        "host_company" : company,
        "first_name": 'sadf',
        "last_name": 'sadf',
        "email": 'sadf'    
    }

    print(f'member object: {member_object}')

    return member_object
    
if __name__ == '__main__':
    get_meetup()
    print("CSV generation complete!")