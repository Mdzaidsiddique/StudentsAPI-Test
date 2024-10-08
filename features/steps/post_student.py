import requests
from behave import *

payload_data = {
    "name": "Shoaib",
    "location": "India",
    "courses": [
        "Power BI",
        "Python",
        "My SQL"
    ]
}

base_URL = "http://localhost:3000/" 

@given(u'I have the base URL and payload data of the StudentAPI')
def step_impl(context):
    context.url = base_URL
    context.pl_data = payload_data

@when(u'I send a POST request to "{endpoint}"')
def step_impl(context, endpoint):
    res = requests.post(f"{context.url}{endpoint}", json=context.pl_data)
    context.response = res

@then(u'I should receive a 201 status code')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"

@then(u'the response should contain that particular student data')
def step_impl(context):
    # Parse the JSON response
    response_data = context.response.json()  # Get the JSON content
    
    # Print the content for debugging
    print(response_data)
    
    # Assertions to verify the returned data
    assert response_data['name'] == 'Shoaib', f"Expected name to be 'Shoaib', but got '{response_data.get('name')}'"
    assert response_data['location'] == 'India', f"Expected location to be 'India', but got '{response_data.get('location')}'"
    assert response_data['courses'] == payload_data['courses'], f"Expected courses to be {payload_data['courses']}, but got {response_data.get('courses')}"
