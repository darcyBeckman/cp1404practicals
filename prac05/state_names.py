"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
LOWERCASE_CODE_TO_NAME = {v.lower(): k for v, k in CODE_TO_NAME.items()}

state_code = input("Enter short state: ").lower()
while state_code != "":
    if state_code in LOWERCASE_CODE_TO_NAME:
        print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").lower()

for state in CODE_TO_NAME:
    print(f"{state:3} is {CODE_TO_NAME[state]}")