import requests
from behave import given, when, then

BASE_URL = "http://localhost:3000"

@given('I have the base URL of the StudentAPI')
def step_given_base_url(context):
    context.url = BASE_URL

@when('I send a GET request to "{endpoint}"')
def step_when_send_get_request(context, endpoint):
    response = requests.get(f"{context.url}{endpoint}")
    context.response = response

@then('I should receive a 200 status code')
def step_then_check_status_code(context):
    assert context.response.status_code == 200

@then('the response should contain student data')
def step_then_check_student_data(context):
    data = context.response.json()
    print(data)
    assert data[0]['name'] == 'John'
