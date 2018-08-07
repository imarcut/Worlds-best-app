Feature: Login
  In order to use the app the user must be able to Login

  Scenario: Login Success
    Given the user access worlds best app
    When the user enters username
    And the user enters password
    And clicks Login
    Then the user is presented with a welcome message

  Scenario: Login Incorrect credentials
    Given the user access worlds best app
    When the user has the incorrect credentials
    And clicks Login
    Then the user is presented with an error message

  Scenario: Login Correct Username and Incorrect password
    Given the user access worlds best app
    When the user has correct username and incorrect password
    And clicks Login
    Then the user is presented with an error message

  Scenario: Login Correct Username and no password
    Given the user access worlds best app
    When the user has correct username and no password
    And clicks Login
    Then the user is presented with an error message

  Scenario: Login no Username and correct password
    Given the user access worlds best app
    When the user has no username and correct password
    And clicks Login
    Then the user is presented with an error message

  Scenario: Login with blank credentials
    Given the user access worlds best app
    When the user has blank credentials
    And clicks Login
    Then the user is presented with an error message





