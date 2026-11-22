
print("====================================")
print("       PASSWORD STRENGTH CHECKER")
print("====================================")

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(not c.isalnum() for c in password):
    score += 1

print("\nPassword Analysis:")

if score <= 2:
    print("Strength: WEAK")
elif score <= 4:
    print("Strength: MEDIUM")
else:
    print("Strength: STRONG")

print("Score:", score, "/ 5")

if score < 5:
    print("Suggestion: Improve your password using")
    print("letters, numbers and special characters.")
else:
    print("Great! All checks passed.")

print("====================================")
