*** Settings ***
Documentation       Login keywords for the authentication test suite.

Library             Browser


*** Variables ***
${HEADLESS}                 True    # Override via VS Code RobotCode settings or --variable HEADLESS:False
${USERNAME_SELECTOR}        css=[data-test="username"]
${PASSWORD_SELECTOR}        css=[data-test="password"]
${LOGIN_BTN_SELECTOR}       css=[data-test="login-button"]
${ERROR_MSG_LOCATOR}        css=[data-test="error"]

*** Keywords ***
Open Login Page
    [Arguments]    ${url}
    New Browser    headless=${HEADLESS}
    New Page    ${url}
    Get Title    ==    Swag Labs

Enter Credentials
    [Arguments]    ${username}    ${password}
    Fill Text    ${USERNAME_SELECTOR}    ${username}
    Fill Text    ${PASSWORD_SELECTOR}    ${password}

Submit Login Form
    Click    ${LOGIN_BTN_SELECTOR}

Verify Login Success
    Get Url    ==    https://www.saucedemo.com/inventory.html

Verify Invalid Login
    [Arguments]    ${expected_error}
    Get Text    ${ERROR_MSG_LOCATOR}    ==    ${expected_error}
