*** Settings ***
Library    keywords/ui_library.py
Resource    data/test_data.robot
Resource    steps/login_steps.robot
Test Teardown    Close Browser

*** Test Cases ***
Successful Login
    [Tags]    smoke
    User Opens Login Page
    User Logs In As Standard User
    Login Should Succeed

Locked Out User Cannot Login
    [Tags]    smoke
    User Opens Login Page
    User Logs In As Locked User
    Locked Out Error Should Be Shown