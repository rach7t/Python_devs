
CORRECT_PIN = "4321"

maximum_attempts = 3
attempts = 0
authenticated = False

print("--- Welcome to the ATM ---")

while attempts < maximum_attempts:
    entered_pin = input(f"Enter your 4-digit PIN (Attempt {attempts + 1}/{maximum_attempts}): ").strip()
    attempts += 1
    
    if entered_pin == CORRECT_PIN:
        authenticated = True
        break
    else:
        remaining = maximum_attempts - attempts
        if remaining > 0:
            print(f"Incorrect PIN. You have {remaining} attempt(s) left.\n")


if authenticated:
    print("\nPIN Verified Successfully! Access Granted.")
else:
    print("\nAccount Locked! You have exceeded the maximum number of attempts.")