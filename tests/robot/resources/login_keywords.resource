*** Settings ***
Library    Browser

*** Variables ***
${URL}                  https://testerbud.com/practice-login-form
${VALID_USER}           user@premiumbank.com
${VALID_PASS}           Bank@123
${USERNAME_SELECTOR}    css=#formBasicEmail
${PASSWORD_SELECTOR}    css=#formBasicPassword
${LOGIN_BTN_SELECTOR}   css=button[type='submit']
${SUCCESS_MSG_LOCATOR}  css=.alert-success

*** Keywords ***
Open Login Page
    New Browser    headless=True
    New Page       ${URL}
    Get Title      contains    Login Automation Practice Page

Enter Credentials
    [Arguments]    ${username}    ${password}
    Fill Text    ${USERNAME_SELECTOR}    ${username}
    Fill Text    ${PASSWORD_SELECTOR}    ${password}

Submit Login Form
    Click    ${LOGIN_BTN_SELECTOR}

Verify Login Success
    Get Text    ${SUCCESS_MSG_LOCATOR}    contains    Login Successful
