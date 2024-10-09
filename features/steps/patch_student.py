import requests
from behave import *

# Updated payload for PATCH request
payload_data = {
    "location": "Kanpur, India"
}

base_URL = "http://localhost:3000/"

# Step for setting up the base URL and payload
@given(u'I have the base URL and updated student data with patch')
def step_impl(context):
    context.url = base_URL
    context.pl_updated_data = payload_data

@when(u'I send a PATCH request to "/students/9152"')
def step_impl(context):
    # Use the full endpoint directly here
    endpoint = "/students/9152"
    res = requests.patch(f"{context.url}{endpoint}", json=context.pl_updated_data)
    context.response = res

# Step for asserting the updated student data
@then(u'the response should contain updated student data with patch')
def step_impl(context):
    response_data = context.response.json()
    print(response_data)
    assert response_data['location'] == 'Kanpur, India', f"Expected location to be 'Kanpur, India', but got '{response_data.get('location')}'"

# Step for checking the status code
@then(u'I should receive a 200 status code after patch')
def step_impl(context):
    assert context.response.status_code == 200