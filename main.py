from js import document
import random

def check_eligibility():
    registration = document.getElementById("registration").value
    medical = document.getElementById("medical").value
    grade = int(document.getElementById("grade").value)
    result = document.getElementById("result")

    teams = [
        "Blue Bears",
        "Red Bulldogs",
        "Yellow Tigers",
        "Green Hornets"
    ]

    if registration != "yes":
        result.innerText = "You are not eligible. Please register online."

    elif medical != "yes":
        result.innerText = "You are not eligible. Please secure a medical clearance."

    elif grade < 7 or grade > 10:
        result.innerText = "You are not eligible. Intramurals are only for Grades 7–10."

    else:
        team = random.choice(teams)
        result.innerText = (
            "Congratulations! You are eligible to join the Intramurals. "
            f"Your team is {team}."
        )

