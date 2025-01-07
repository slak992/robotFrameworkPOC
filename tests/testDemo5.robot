*** Settings ***
Library     SeleniumLibrary
Library    Dialogs
Resource    config/base.robot
Resource    config/resources.robot
Test Setup      Open the browser and launch the login page
Test Teardown   Close Browser

*** Variables ***

@{order_list}       Nokia Edge

*** Test Cases ***
Complete the order
    Login to home page
    add items to the cart       ${order_list}
    verify elements in the cart     ${order_list}   True
    &{country_details}=     Create Dictionary       Ind=India
    Select the location and click Puchase button        ${country_details}
    Pause Execution
