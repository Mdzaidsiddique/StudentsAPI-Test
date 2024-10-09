import requests
from behave import *

base_URL = "http://localhost:3000/"

@given(u'I have the base URL for the StudentAPI for delete operation')
def step_impl(context):
    context.url = base_URL

@when(u'I send a DELETE request to "/students/9152"')
def step_impl(context):
    # Sending DELETE request to delete the student with ID 9152
    endpoint = "/students/9152"
    res = requests.delete(f"{context.url}{endpoint}")
    context.response = res

@then(u'I should receive a 200 status code after delete')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"

@then(u'the student with ID "9152" should be deleted')
def step_impl(context):
    # Verifying the student has been deleted by trying to retrieve the same student
    endpoint = "/students/9152"
    res = requests.get(f"{context.url}{endpoint}")
    assert res.status_code == 404, f"Expected status code 404 for non-existing student, but got {res.status_code}"
