Feature: Create a student

  Scenario: Successfully create a new student
    Given I have student data
      | Name  | location | courses           |
      | Atif  | India    | Java, SQL, Spring |
    When I send a POST request to "/students" to create a student
    Then the student should be created successfully
    And I should get status code 201 of created
