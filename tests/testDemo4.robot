*** Settings ***
Library     SeleniumLibrary
Library    Collections
Resource    config/resources.robot
Library     BuiltIn
Library    OperatingSystem
Library    Dialogs
Resource       config/base.robot
Test Setup      Open the browser and launch the login page
Test Teardown   Close Browser

*** Variables ***

@{check_in_items}           Samsung Note 8      Blackberry

*** Test Cases ***

Verify the functionality for adding items to the cart
    [Tags]      smoke   regression
    Login to home page
    add items to the cart       ${check_in_items}
    verify elements in the cart     ${check_in_items}



    
    


