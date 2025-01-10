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
Check the items displayed in the home page
    [Tags]      regression
    Login to home page
    The homepage should contain the items from the expected list



Verify the login and fail for rerun
    Enter username and password     scp     XXX
    Click Signin and user should successfully login
    
    


