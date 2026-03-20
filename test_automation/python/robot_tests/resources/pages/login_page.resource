*** Settings ***
Library    ../keywords/ui_library.py
Resource   ../../data/test_data.robot

*** Keywords ***
User Opens Login Page
    Open Browser To Login

User Enters Standard Credentials
    Login With Credentials    ${STANDARD_USER}    ${PASSWORD}

User Enters Locked User Credentials
    Login With Credentials    ${LOCKED_OUT_USER}    ${PASSWORD}

Login Should Succeed
    Verify Login Successful

Locked Out Error Should Be Shown
    ${error}=    Get Login Error Message
    Should Contain    ${error}    locked out
