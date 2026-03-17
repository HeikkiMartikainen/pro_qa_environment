*** Settings ***
Documentation       Login keywords for the authentication test suite.

Library             Browser


*** Variables ***
${HEADLESS}                 True    # Override via VS Code RobotCode settings or --variable HEADLESS:False
${USERNAME_SELECTOR}        css=#formBasicEmail
${PASSWORD_SELECTOR}        css=#formBasicPassword
${LOGIN_BTN_SELECTOR}       css=button[type='submit']
${SUCCESS_MSG_LOCATOR}      css=.alert-success
${ERROR_MSG_LOCATOR}        css=.alert-danger
${FORGET_PASSWORD_LINK_SELECTOR}    css=a[href='/forget-password']
${REGISTER_LINK_SELECTOR}           css=a[href='/register']

*** Keywords ***
Open Login Page
    [Arguments]    ${url}
    New Browser    headless=${HEADLESS}
    New Page    ${url}
    Get Title    contains    Login Automation Practice Page

Enter Credentials
    [Arguments]    ${username}    ${password}
    Fill Text    ${USERNAME_SELECTOR}    ${username}
    Fill Text    ${PASSWORD_SELECTOR}    ${password}

Submit Login Form
    Click    ${LOGIN_BTN_SELECTOR}

Verify Login Success
    Get Text    ${SUCCESS_MSG_LOCATOR}    contains    Login Successful

Verify Invalid Login
    Get Text    ${ERROR_MSG_LOCATOR}    contains    Invalid email id and password

Verify UI Elements Are Visible
    Get Element States    ${USERNAME_SELECTOR}    contains    visible
    Get Element States    ${PASSWORD_SELECTOR}    contains    visible
    Get Element States    ${LOGIN_BTN_SELECTOR}    contains    visible
    Get Element States    ${FORGET_PASSWORD_LINK_SELECTOR}    contains    visible
    Get Element States    ${REGISTER_LINK_SELECTOR}    contains    visible

Verify Login Button Is Enabled
    Get Element States    ${LOGIN_BTN_SELECTOR}    contains    enabled

Verify Empty Fields Error
    Get Text    ${ERROR_MSG_LOCATOR}    contains    Email and Password are required

Verify Password Field Is Masked
    Get Attribute    ${PASSWORD_SELECTOR}    type    ==    password

Verify Password Is Required Error
    Get Text    ${ERROR_MSG_LOCATOR}    contains    Password is required

Enter Invalid Email Format
    Fill Text    ${USERNAME_SELECTOR}    abc123

Verify Invalid Email Format Error
    ${message}=    Get Property    ${USERNAME_SELECTOR}    validationMessage
    Should Contain    ${message}    Please include an '@' in the email address.
