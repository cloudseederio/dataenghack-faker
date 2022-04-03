from faker import Faker
import datetime
import random
import json
import random

cities = [
    'Sydney',
    'Melbourne',
    'Brisbane',
    'Perth'
]

def stream_write_json(json_object):
    with open('outputs/companies.json','a') as f:
        f.write(json.dumps(json_object))
        f.write("\u000a")


def get_cities():
    random_cities = random.choices(
        population=cities,
        weights=[0.5, 0.3, 0.1, 0.1],
        k=300
    )
    for city in random_cities:
        result = generate_companies(city)
        stream_write_json(result)

def get_state_postcode(city):
    state = ''
    first_postcode_digit = '0'
    if city == 'Sydney':
        state = 'NSW'
        first_postcode_digit = '2'
    elif city == 'Melbourne':
        state = 'VIC'
        first_postcode_digit = '3'
    elif city == 'Brisbane':
        state = 'QLD'
        first_postcode_digit = '4'
    elif city == 'Perth':
        state = 'WA'
        first_postcode_digit = '7'
    else:
        state = 'Other'
        first_postcode_digit = '0'
    return state, first_postcode_digit

def generate_companies(city):
    fake = Faker('en_AU')
    country = "Australia"
    company_name = fake.company()

    state, first_postcode_digit = get_state_postcode(city)

    # a Python object (dict):
    company_object = {
        "company_name": company_name,
        "street_address" : fake.street_address(),
        "city" : city,
        "state" : state,
        "post_code" : first_postcode_digit + fake.postcode()[0:3],
        "country" : country,
    }

    print(f'company object: {company_object}')

    return company_object
    
if __name__ == '__main__':
    get_cities()
    print("CSV generation complete!")