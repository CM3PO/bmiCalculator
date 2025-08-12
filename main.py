import time

def calculate_bmi(weight_lbs, height_feet, height_inches):
    """
    Calculates BMI (Body Mass Index) using weight in pounds and height in feet and inches.

    Args:
        weight_lbs (float): Weight in pounds.
        height_feet (int): Height in feet.
        height_inches (int): Height in inches.

    Returns:
        float: Calculated BMI.
    """
    total_inches = (height_feet * 12) + height_inches
    bmi = (weight_lbs / (total_inches ** 2)) * 703
    return bmi

def interpret_bmi(bmi):
    """
    Interprets the BMI value and returns a corresponding category.

    Args:
        bmi (float): Calculated BMI.

    Returns:
        str: BMI category (Underweight, Normal, Overweight, or Obese).
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# --- USER INPUT SECTION ---

# Weight input
while True:
    try:
        weight_lbs = float(input("Enter your weight in pounds: "))
        if weight_lbs <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid weight in pounds (positive number).")

# Height (feet) input
while True:
    try:
        height_feet = int(input("Enter your height in feet: "))
        if height_feet < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter your height in feet (non-negative integer).")

# Height (inches) input
while True:
    try:
        height_inches = int(input("Enter your height in inches (0–11): "))
        if not (0 <= height_inches <= 11):
            raise ValueError
        break
    except ValueError:
        print("Please enter your height in inches (between 0 and 11).")

# Gender input
while True:
    gender = input("Enter your gender (Male, Female, or Prefer not to answer): ").strip().lower()
    if gender in ["male", "female", "prefer not to answer"]:
        break
    else:
        print("Please enter 'Male', 'Female', or 'Prefer not to answer'.")

# --- BMI CALCULATION AND INTERPRETATION ---

bmi_result = calculate_bmi(weight_lbs, height_feet, height_inches)
bmi_category = interpret_bmi(bmi_result)

# --- OUTPUT RESULTS ---

print(f"\nGender: {gender.title()}")
print(f"Your BMI is: {bmi_result:.2f}")
print(f"You are in the {bmi_category} category.")

time.sleep(2)

# --- OPTIONAL HEALTH SUGGESTIONS ---

print("\nWould you like any suggestions on how to improve your health?")
while True:
    suggestions = input("Enter 'Y' or 'N': ").strip().lower()
    if suggestions in ['y', 'n']:
        break
    else:
        print("Please enter 'Y' or 'N'.")

if suggestions == 'y':
    print("\nWhat would you like help with?")
    print("Enter 'F' for Fitness, 'N' for Nutrition, or 'O' for Other.")

    while True:
        help_topic = input("Your choice: ").strip().lower()
        if help_topic in ['f', 'n', 'o']:
            break
        else:
            print("Please enter 'F', 'N', or 'O'.")

    if help_topic == 'f':
        print("\nFitness Tip: Aim for at least 30 minutes of moderate physical activity most days. Start with walking, stretching, or light strength training.")

    elif help_topic == 'n':
        print("\nNutrition Tip: Include a variety of colorful fruits and vegetables in your meals, drink plenty of water, and limit processed foods.")

    elif help_topic == 'o':
        custom_request = input("\nPlease describe what you'd like help with: ")
        print("Thank you! We'll send your message to a certified trainer.")
        # Simulated email sending
        print(f"\n[Simulated Email Sent]\nSubject: Help Request\nMessage: {custom_request}")

# --- END OF PROGRAM ---
