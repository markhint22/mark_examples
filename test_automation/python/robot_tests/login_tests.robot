*** Settings ***
Resource    resources/flows/auth_flow.resource
Resource    resources/pages/login_page.resource
Test Teardown    Close Browser

*** Test Cases ***
Successful Login
    [Tags]    smoke    login
    User Logs In As Standard User
    Login Should Succeed

Locked Out User Cannot Login
    [Tags]    smoke    login
    Locked User Attempts Login
    Locked Out Error Should Be Shown