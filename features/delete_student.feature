Feature: Delete a student's information
  As an API user
  I want to be able to delete a student from the system
  So that the student information is no longer available

  Scenario: Successfully delete a student by ID
    Given I have the base URL for the StudentAPI for delete operation
    When I send a DELETE request to "/students/9152"
    Then I should receive a 200 status code after delete
    And the student with ID "9152" should be deleted
