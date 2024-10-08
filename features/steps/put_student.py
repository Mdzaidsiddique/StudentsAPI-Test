import requests
from behave import *

payload_data = {
    "name": "Mohd Salman Mansoori",
    "location": "India",
    "courses": [
        "Power BI",
        "Python",
        "My SQL",
        "Poetry"
    ]
}

base_URL = "http://localhost:3000/" 

@given(u'I have the base URL and updated student data')
def step_impl(context):
    context.url = base_URL
    context.pl_updated_data = payload_data


@when(u'I send a PUT request to "{endpoint}" with "{id}"')
def step_impl(context, endpoint,id):
    res = requests.put(f"{context.url}{endpoint}{id}", json= context.pl_updated_data)
    context.response = res

@then(u'the response should contain updated student data')
def step_impl(context):
    response_data = context.response.json()
    print(response_data)
    assert response_data['name'] == 'Mohd Salman Mansoori', f"Expected name to be 'Mohd Salman Mansoori', but got '{response_data.get('name')}'"