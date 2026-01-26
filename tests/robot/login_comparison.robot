*** Settings ***
Resource    resources/login_keywords.resource

*** Test Cases ***
Login To TesterBud
    [Documentation]    Compares Robot Framework Browser library with Playwright.
    Open Login Page
    Enter Credentials    ${VALID_USER}    ${VALID_PASS}
    Submit Login Form
    Verify Login Success
