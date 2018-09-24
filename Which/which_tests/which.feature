Feature: To test the functionlaity of the webpage

Scenario: To verify if the website loads when the user enters the URL
    Given I have the URL
   Then The website should load successfully


 Scenario: To verify if the 'best buys' option works
   Given I have the URL
   When I click on Best Buys
   Then The page should display Best Buy items

 Scenario: To verify if the 'Dont Buy' option works
    Given I have the URL
    When  I click on Dont Buys
    Then The page should display the dont buy content


 Scenario: To verify if the 'Screen Size' option works
    Given I have the URL
    When I click on the different Screen size
    Then The page should display the Screen Size content


 Scenario: To verify of the brands option works
    Given I have the URL
    When I select a brand
    Then The page should display the selected brands



