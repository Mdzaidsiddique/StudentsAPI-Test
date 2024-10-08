Feature: Student API Automation

Scenario: Get student information
   Given I have the base URL of the StudentAPI
   When I send a GET request to "/students"
   Then I should receive a 200 status code
   And the response should contain student data
