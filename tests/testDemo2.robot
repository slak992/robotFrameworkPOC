*** Settings ***
Library     SeleniumLibrary
Library     DataDriver      file=resources/test_data.csv
Resource    config/resources.robot
Resource    config/base.robot
Test Setup      Open the browser and launch the login page
Test Template   Login with username and password
Test Teardown   Close Browser


*** Variables ***
${incorrect_login_msg_locator}      css:div.alert
${expected_alert_message}       Incorrect username/password.
${cart_title_locator}       xpath://h4[@class='card-title']
@{check_in_items}       Samsung Note 8      Blackberry

*** Test Cases ***
#Login with username ${user_name_test_data} and password ${password_test_data}
Login with username ${user_name_test_data} and password ${password_test_data}



*** Keywords ***

Login with username and password
    [Arguments]     ${user_name_test_data}     ${password_test_data}
    Enter username and password     ${user_name_test_data}      ${password_test_data}
    Click Button    signInBtn
    Wait Until Element Is Visible    ${incorrect_login_msg_locator}
    ${unsuccessful_msg}=  Get Text    ${incorrect_login_msg_locator}
    Sleep    5
    Validate the error message      ${unsuccessful_msg}





    
    


