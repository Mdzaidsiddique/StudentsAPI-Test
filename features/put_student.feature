Feature: Update student information

Scenario: Successfully update Student information
    Given I have the base URL and updated student data
    When I send a PUT request to "/students" with "/9152"
    Then I should receive a 200 status code
    And the response should contain updated student data
