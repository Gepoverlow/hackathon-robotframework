*** Settings ***
Library    ./../libraries/HackathonLibrary.py
Library    OperatingSystem

*** Variables ***
${URL}        https://hackthefuture.bignited.be/

*** Test Cases ***
Complete Hackathon
    Open Browser
    Go To Url    ${URL}
    Click Element    center-button    class
    Wait For Element With Id Visible    male    30
    Click Element    male    id
    Click Element With Text    Yes
    Type Element By Placeholder    Enter your name    Bob
    Type Element By Placeholder    Enter your age    33
    Select Country    Belgium  
    Click Element With Text    Start Game
    Click Element    letters    id
    Click Element    close    class
    Wait For Element With Id Visible    crystal    10
    Click Element    crystal    id
    Wait For Element With Id Visible    image-crystal    5
    Click Element    image-crystal    id
    Wait For Element With Id Visible    randomValuesScreen    15
    ${values}=    Get Switch Values   randomValue 
    Solve Switches    ${values}
    Click Element    button    id
    Click Element    submarine    id
    Wait For Element With Id Visible    instructions    10
    Solve Arrows
    Wait For Url Contains    /crash    15
    Click Element    square        class    True
    Wait For Element With Id Visible    square-0    5
    Solve Doors
    Wait For Element With Id Visible    draggable-cubes-container    5
    Solve Cave Puzzle
    Wait For Element With Class Visible    cystal-outside    5
    Close Browser
