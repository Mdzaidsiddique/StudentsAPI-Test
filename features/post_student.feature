Feature: Add a new Student

Scenario: Successfully student information
    Given I have the base URL and payload data of the StudentAPI
    When I send a Post request to "/students"
    Then I should receive a 201 status code
    And the response should contain that particular student data