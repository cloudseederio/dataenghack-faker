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

Warehouses = [
    "Redshift",
    "Snowflake",
    "Big Query",
    "Databricks",
    "Delta Lake",
    "SQL Server",
    "Athena",
    "Azure Synapse",
    "Teradata",
    "Presto",
    "Apache Druid"
]

Languages = [
    "Python",
    "Scala",
    "Java",
    "Go",
    "Node.js",
    "R",
    "SQL",
    "C#",
    "Perl",
    "Julia",
    "Kotlin",
    "Rust"
]

Frameworks = [
    "Airflow",
    "Spark",
    "Kafka",
    "dbt",
    "Argo",
    "Dataflow",
    "dagster",
    "Matillion",
    "Pandas",
    "Pulsar",
    "Flink",
    "NiFi",
    "Hive"
]

Clouds = [
    "AWS",
    "Google Cloud",
    "Azure",
    "AliCloud",
    "Oracle",
    "On Prem",
    "IBM Cloud",
    "Open Stack"
]

Vendors = [
    "Fivetran",
    "Snowflake",
    "Databricks",
    "Imply",
    "Datastax",
    "Neo4j",
    "dbt Cloud",
    "AWS",
    "Azure"
]

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

meetup_members_df = pd.read_json('outputs/meetup_members.json', lines=True)
print('meetup_members_df',meetup_members_df)
survey_sample = meetup_members_df.sample(2500).to_numpy()
print('survey_sample',survey_sample)

def get_survey_response():
    for respondee in survey_sample:
        print('respondee',respondee)
        result = generate_survey_response(respondee)
        stream_write_json(result)

def stream_write_json(json_object):
    with open('outputs/survey_responses.json','a') as f:
        f.write(json.dumps(json_object))
        f.write("\u000a")


def generate_survey_response(respondee):

    # a Python object (dict):
    survey_object = dict(enumerate(respondee.flatten(), 1))
    survey_object['warehouses'] = random.choices(Warehouses, k=1)
    survey_object['languages'] = random.choices(Languages, k=2)
    survey_object['frameworks'] = random.choices(Frameworks, k=2)
    survey_object['clouds'] = random.choices(Clouds, k=1)
    survey_object['vendors'] = random.choices(Vendors, k=3)

    print(f'member object: {survey_object}')

    return survey_object
    
if __name__ == '__main__':
    get_survey_response()
    print("CSV generation complete!")