*** Settings ***
Resource    ../pages/login_page.resource

*** Keywords ***
User Logs In As Standard User
    User Opens Login Page
    User Enters Standard Credentials

Locked User Attempts Login
    User Opens Login Page
    User Enters Locked User Credentials
    