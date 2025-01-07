*** Settings ***
Library     SeleniumLibrary
Library    Collections
Resource    config/resources.robot
Library     BuiltIn
Library    OperatingSystem
Library    Dialogs
Test Setup      Open the browser and launch the login page
Test Teardown   Close Browser
Resource    config/base.robot

*** Test Cases ***
Parameterised Test case
    [Template]  Check the unsucessful login scnearios
    scp         learning
    rahulshettyacademy      kjndsj
    @3$         sdfbhd


Check whether the cart is displayed in the home page
    [Tags]      smoke
    Login to home page
    Sleep    5
Check the items displayed in the home page
    Login to home page
    The homepage should contain the items from the expected list

Verify the functionality for adding items to the cart
    Login to home page
    From the home page, check for the items in expected list and add it to the cart
    Go to the cart and verify the products
Verify the login form data fields
    Enter username and password
    Select user radio button
    Select Teacher from the dropdown box
    Check the agreement box
    Click Signin and user should successfully login















    
    


