*** Settings ***
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
*** Variables ***

${cart_title_locator}       xpath://h4[@class='card-title']

@{check_in_items}       Samsung Note 8      Blackberry

*** Keywords ***

The homepage should contain the items from the expected list
    ${expected_list}=        Create List        iphone X    Samsung Note 8      Nokia Edge      Blackberry
    ${cart_list_webElements}=   Get WebElements    ${cart_title_locator}
    @{actual_list}=     Create List
    FOR  ${each_ele}    IN      @{cart_list_webElements}
        ${item_title}=  Get Text    ${each_ele}
        Append To List    ${actual_list}    ${item_title}

    END
    Log    ${actual_list}
    Log    ${expected_list}
    Lists Should Be Equal    ${actual_list}    ${expected_list}

From the home page, check for the items in expected list and add it to the cart

    ${item_dic}=    Create Dictionary
    ${cart_list_webElements}=   Get WebElements    ${cart_title_locator}
    ${index}=   Set Variable    1
    FOR  ${each_ele}    IN      @{cart_list_webElements}
        ${item_title}=  Get Text    ${each_ele}
        Set To Dictionary    ${item_dic}    ${item_title}=${index}
        ${index}=   Evaluate    ${index}+1

    END
    FOR    ${element}    IN    @{check_in_items}
        ${dic_val_test}=       Set Variable    ${item_dic}[${element}]
        Click Element    xpath:(//div[@class='card-footer'])[${dic_val_test}]/button
    END
