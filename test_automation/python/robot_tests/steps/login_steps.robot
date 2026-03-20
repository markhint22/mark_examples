*** Settings ***
Library    ../keywords/ui_library.py
Resource    ../data/test_data.robot

*** Keywords ***
User Opens Login Page
    Open Browser To Login

User Logs In As Standard User
    Login With Credentials    ${STANDARD_USER}    ${PASSWORD}

User Logs In As Locked User
    Login With Credentials    ${LOCKED_OUT_USER}    ${PASSWORD}

Login Should Succeed
    Verify Login Successful

Locked Out Error Should Be Shown
    ${error}=    Get Login Error Message
    Should Contain    ${error}    locked out
