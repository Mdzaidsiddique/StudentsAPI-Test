Feature: Update of student information with patch

Scenario: Successfully updated single Student information with patch
    Given I have the base URL and updated student data with patch
    When I send a PATCH request to "/students/9152"
    Then I should receive a 200 status code after patch
    And the response should contain updated student data with patch