Feature: Handle storing, retrieving and deleting customer details
Scenario: Retrive a customers details
Given some users are in the system
When I retrive the customer 'david01'
Then I should get a '200' response
And the following user details are returned:
    | name |
    | David Sale |

