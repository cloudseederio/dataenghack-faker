from faker import Faker
import datetime
import random
import json
import random
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

companies_df = pd.read_json('outputs/companies.json', lines=True)
sydney_company_name = companies_df[(companies_df.city=="Sydney")].company_name.to_numpy()
melbourne_company_name = companies_df[(companies_df.city=="Melbourne")].company_name.to_numpy()
brisbane_company_name = companies_df[(companies_df.city=="Brisbane")].company_name.to_numpy()
perth_company_name = companies_df[(companies_df.city=="Perth")].company_name.to_numpy()

def random_company(city):
    if city == "Sydney":
        return random.choices(sydney_company_name)
    elif city == "Melbourne":
        return random.choices(melbourne_company_name)
    elif city == "Brisbane":
        return random.choices(brisbane_company_name)
    elif city == "Perth":
        return random.choices(perth_company_name)
    else:
        return 'Unknown'

def stream_write_json(json_object):
    with open('outputs/meetup_events.json','a') as f:
        f.write(json.dumps(json_object))
        f.write("\u000a")

def get_meetup():
    x = 1
    while x < 60:
        for city in cities:
            date_format = '%Y-%m-%d'
            dtObj = datetime.strptime(start_date, date_format)
            future_date = dtObj + relativedelta(months=x)
            # print(f'city: {city}')
            city_name = city['city']
            creation_date = datetime.strptime(city['creation_date'], date_format)
            if future_date >= creation_date:
                day_date = random.randint(1,28)
                meetup_date = f'{future_date.year}-{future_date.month}-{day_date}'
                print(f'{city_name} is on {meetup_date}')
                result = generate_meetup_events(city_name, random_company(city_name), meetup_date, future_date.strftime("%B"))
                stream_write_json(result)
        x += 1

def generate_meetup_events(city, company, date, month):
    fake = Faker('en_AU')

    # a Python object (dict):
    event_object = {
        "city": city,
        "event_name": f'{city} DataEng meetup, {month} Edition',
        "date": date,
        "host_company" : company[0],
    }

    print(f'company object: {event_object}')

    return event_object
    
if __name__ == '__main__':
    get_meetup()
    print("CSV generation complete!")