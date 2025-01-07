*** Settings ***
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
Library    Dialogs
Library    String
*** Variables ***

${location_box}     country
${country_list_locator}     css:div.suggestions ul li a
${purchase_button}      xpath://input[@value='Purchase']
${success_message_locator}      css:div.alert-success
${expected_success_message}     Success! Thank you! Your order will be delivered in next few weeks :-).

*** Keywords ***

Select the location and click Puchase button
    [Arguments]     ${location}
    Log    ${location}
    ${search_key_list}=        Get Dictionary Keys     ${location}
    ${country_list}=         Get Dictionary Values    ${location}
    ${expected_country_name_input}=     Get From List    ${search_key_list}    0
    ${expected_country_name}=   Get From List    ${country_list}    0
    Wait Until Page Contains Element    country
    Input Text    country    ${expected_country_name_input}
    Wait Until Page Contains Element    ${country_list_locator}     timeout=10
    ${country_webelements}=     Get WebElements    ${country_list_locator}
    FOR    ${element}    IN    @{country_webelements}
        ${country_name}=        Get Text    ${element}
        IF    $country_name == $expected_country_name
              Click Element    ${element}
              Exit For Loop
        END

    END

    ${selected_country_name}=   Get Value    ${location_box}
    Should Be Equal As Strings    ${selected_country_name}    ${expected_country_name}
    Click Element    ${purchase_button}
    ${success_message}=     Get Text    ${success_message_locator}
    ${cleared_x_string}=    Replace String      ${success_message}    	×       ${EMPTY}
    ${cleared_newline_string}=    Replace String      ${cleared_x_string}    	\n       ${EMPTY}
    Log    ${cleared_newline_string}
    Should Be Equal As Strings    ${cleared_newline_string}    ${expected_success_message}
    




