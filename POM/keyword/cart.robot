*** Settings ***
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
*** Variables ***

${cart_title_locator}       xpath://h4[@class='card-title']

@{check_in_items}       Samsung Note 8      Blackberry

*** Keywords ***

Go to the cart and verify the products
    Click Element    xpath://a[contains(text(),'Checkout')]
    Wait Until Element Is Visible    xpath://button[contains(text(),'Checkout')]

    @{cart_items}=  Create List
    @{cart_item_webelements}=   Get WebElements    xpath://h4[@class='media-heading']/a
    FOR    ${cart_item}    IN    @{cart_item_webelements}
        ${item_title}=  Get Text    ${cart_item}
        Append To List    ${cart_items}     ${item_title}
    END
    Log    ${cart_items}

    Lists Should Be Equal    ${cart_items}    ${check_in_items}

