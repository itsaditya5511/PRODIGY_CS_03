import re

def assess_password_strength(password):
    # Criteria for password strength
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    # Calculate score based on criteria met
    score = sum(criteria.values())

    # Provide feedback
    feedback = []

    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Password should include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Password should include at least one lowercase letter.")
    if not criteria["digit"]:
        feedback.append("Password should include at least one digit.")
    if not criteria["special_char"]:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*()).")

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "strength": strength,
        "feedback": feedback
    }

# Example usage
password = "P@ssw0rd!"
result = assess_password_strength(password)

print(f"Password Strength: {result['strength']}")
if result['feedback']:
    print("Feedback:")
    for comment in result['feedback']:
        print(f" - {comment}")
