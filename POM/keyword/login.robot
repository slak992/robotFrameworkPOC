*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${default_username}        rahulshettyacademy
${default_password}         learning
${username_locator}     username
${password_locator}     password
${sign_in_locator}      signInBtn
${incorrect_login_msg_locator}      css:div.alert

${expected_alert_message}       Incorrect username/password.

${cart_locator}     xpath://a[contains(text(),'Checkout')]
*** Keywords ***
Check the unsucessful login scnearios
    [Arguments]     ${username_parameterised}       ${password_parameterised}
    Enter username and password     ${username_parameterised}      ${password_parameterised}
    Click Button    signInBtn
    Wait Until Element Is Visible    ${incorrect_login_msg_locator}
    ${unsuccessful_msg}=  Get Text    ${incorrect_login_msg_locator}
    Sleep    5
    Validate the error message      ${unsuccessful_msg}

Enter username and password
    [Arguments]     ${user_name}=${default_username}        ${password}=${default_password}
    Input Text    ${username_locator}    ${user_name}
    Input Password    ${password_locator}    ${password}
Validate the error message
    [Arguments]     ${unsuccessful_msg}
    Log    ${unsuccessful_msg}
    Should Be Equal As Strings    ${unsuccessful_msg}    ${expected_alert_message}
Login to home page
    Input Text    ${username_locator}    ${default_username}
    Input Password    ${password_locator}    ${default_password}
    Click Button    ${sign_in_locator}
    Wait Until Element Is Visible    ${cart_locator}

#Enter invalid username and password
#    [Arguments]     ${invalid_username}     ${invalid_password}
#    Input Text    ${username_locator}    ${invalid_username}
#    Input Password    ${password_locator}    ${invalid_password}
#    Click Button    ${sign_in_locator}
#    Wait Until Element Is Visible    ${incorrect_login_msg_locator}
#    ${unsuccessful_msg}=  Get Text    ${incorrect_login_msg_locator}
#    RETURN  ${unsuccessful_msg}
Select user radio button
    Select Radio Button    radio    user
    Wait Until Element Is Visible    okayBtn
    Click Element    okayBtn
    Wait Until Element Is Not Visible    okayBtn
    Radio Button Should Be Set To    radio    user
Select Teacher from the dropdown box
    Select From List By Value    css:Select.form-control    teach
Check the agreement box
    Select Checkbox    terms
    Checkbox Should Be Selected    terms
Click Signin and user should successfully login
    Click Button    signInBtn
    Wait Until Element Is Visible    xpath://a[contains(text(),'Checkout')]
