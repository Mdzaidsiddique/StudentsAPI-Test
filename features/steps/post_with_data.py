import requests
from behave import given, when, then

# Base API URL
API_URL = "http://localhost:3000/"

@given(u'I have student data')
def step_impl(context):
    print("-=-=-=-=zaid")
    print(context.table, type(context.table))
    context.student_data = []
    for row in context.table:
        print(row)
        student = {
            "name": row['Name'],
            "location": row['location'],
            "courses": row['courses'].split(", ")  # Split the courses by comma
        }
        context.student_data.append(student)

@when(u'I send a POST request to "{endpoint}" to create a student')
def step_impl(context, endpoint):
    for student in context.student_data:
        response = requests.post(f"{API_URL}{endpoint}", json=student)
        context.response = response

@then(u'the student should be created successfully')
def step_impl(context):
    assert context.response.status_code == 201, f"Expected status code 201, but got {context.response.status_code}"
    print(f"Student created: {context.response.json()}")

@then(u'I should get status code 201 of created')
def step_impl(context):
    assert context.response.status_code == 201, "Expected status code 201, but got {0}".format(context.response.status_code)
