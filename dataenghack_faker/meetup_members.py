from faker import Faker
import datetime
import random
import json
import random
import faker
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import string


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
    with open('outputs/meetup_members.json','a') as f:
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
                signup_date = f'{future_date.year}-{future_date.month}-{future_date.day}'
                print(f'{city_name} is on {signup_date}')
                result = generate_member(city_name, random_company(city_name)[0], signup_date)
                stream_write_json(result)
        x += 1

def generate_member(city, company, date):
    fake = Faker('en_AU')
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    mobile = fake.phone_number()
    domain_name = company.split(' ')[0].translate((str.maketrans('', '', string.punctuation))).lower()
    company_email = f'{first_name}.{last_name}@{domain_name}.com.au'

    # a Python object (dict):
    member_object = {
        "city": city,
        "signup_date": date,
        "first_name": first_name,
        "last_name": last_name,
        "company" : company,
        "mobile": mobile,
        "email": email,
        "company_email": company_email 
    }

    print(f'member object: {member_object}')

    return member_object
    
if __name__ == '__main__':
    get_member()
    print("CSV generation complete!")