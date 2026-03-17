*** Settings ***
Documentation       Tests for the TesterBud login page.

Resource            resources/login_keywords.resource
Variables           ../../config/variables.py


*** Test Cases ***
TC_Basic_01: Verify login with valid credentials
    Open Login Page    ${BASE_URL}
    Enter Credentials    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Submit Login Form
    Verify Login Success

TC_Basic_02: Verify login with invalid credentials
    Open Login Page    ${BASE_URL}
    Enter Credentials    ${INVALID_USERNAME}    ${INVALID_PASSWORD}
    Submit Login Form
    Verify Invalid Login

TC_Basic_03: Check UI elements
    Open Login Page    ${BASE_URL}
    Verify UI Elements Are Visible

TC_Basic_04: Verify empty fields error and button state
    Open Login Page    ${BASE_URL}
    Verify Login Button Is Enabled
    Submit Login Form
    Verify Empty Fields Error

TC_Basic_05: Verify password field is masked
    Open Login Page    ${BASE_URL}
    Verify Password Field Is Masked

TC_Basic_06: Verify username only error
    Open Login Page    ${BASE_URL}
    Enter Credentials    ${VALID_USERNAME}    ${EMPTY}
    Submit Login Form
    Verify Password Is Required Error

TC_Basic_07: Verify invalid email format
    Open Login Page    ${BASE_URL}
    Enter Invalid Email Format
    Submit Login Form
    Verify Invalid Email Format Error
