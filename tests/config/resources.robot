*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${url}     https://rahulshettyacademy.com/loginpagePractise/
${BROWSER}      chrome


*** Keywords ***
Open the browser and launch the login page
    Create Dictionary       screenshot_dir  ${CURDIR}/../reports/screenshots
    Set Screenshot Directory    ${CURDIR}/../reports/screenshots
    Run Keyword And Ignore Error    Set Selenium Timeout    5
    Open Browser      ${url}        ${BROWSER}
    Maximize Browser Window
    ${status}   ${error}=      Run Keyword And Ignore Error    Wait Until Page Contains Element    css:body    5
    Run Keyword If    '${status}'=='FAIL'    Relaunch browser

Relaunch browser
    Log    Relaunching the browser as it fails to load
    Close Browser
    Open Browser      ${url}        chrome
    Maximize Browser Window



