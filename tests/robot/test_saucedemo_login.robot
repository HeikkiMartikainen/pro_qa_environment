*** Settings ***
Documentation       Tests for the Sauce Demo login page.

Resource            resources/login_keywords.resource
Variables           ../../config/variables.py


*** Test Cases ***
Verify login with valid credentials
    Skip If    not '${SAUCEDEMO_PASSWORD}'    SAUCEDEMO_PASSWORD environment variable not set
    Open Login Page    ${SAUCEDEMO_URL}
    Enter Credentials    ${SAUCEDEMO_STANDARD_USER}    ${SAUCEDEMO_PASSWORD}
    Submit Login Form
    Verify Login Success

Verify login with locked out user
    Skip If    not '${SAUCEDEMO_PASSWORD}'    SAUCEDEMO_PASSWORD environment variable not set
    Open Login Page    ${SAUCEDEMO_URL}
    Enter Credentials    ${SAUCEDEMO_LOCKED_OUT_USER}    ${SAUCEDEMO_PASSWORD}
    Submit Login Form
    Verify Invalid Login    Epic sadface: Sorry, this user has been locked out.

Verify login with invalid credentials
    Open Login Page    ${SAUCEDEMO_URL}
    Enter Credentials    invalid_user    invalid_password
    Submit Login Form
    Verify Invalid Login    Epic sadface: Username and password do not match any user in this service
