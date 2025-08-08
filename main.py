import time

def calculate_bmi(weight_lbs, height_feet, height_inches):
  """ Calculates BMI(Body Mass Index) using weight in pounds and height in feet and inches. 

  Args:
    weight_lbs (float): Weight in pounds.
    height_feet (int): Height in feet.
    height_inches (int): Height in inches.

  Returns:
    float: Calculated BMI.
    """
  # Convert height to total inches
  total_inches = (height_feet *12) + height_inches

  # BMI Formula (using US customary units)
  # BMI = (weight in pounds / (height in inches x height in inches)) * 703
  bmi = (weight_lbs / (total_inches * total_inches)) * 703
  return bmi

def interpret_bmi(bmi):
  """ Interprets the BMI value and returns a corresponding category.
  
  Args: bmi (float): Calculated BMI.
  
  Returns:
  str: BMI category; Underweight, Normal, Overweight."""
  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <=bmi < 25:
    return "Normal"
  elif 25 <= bmi < 30:
    return "Overweight"
  else:
    return "Obese"

# Input from the user with validation
while True:
  try:
    weight_lbs = float(input("Enter your weight in pounds: "))
    if weight_lbs <= 0:
      raise ValueError
    break
  except ValueError:
    print("Please enter a valid weight (no odd numbers).")
    
while True:
  try:
    height_feet = int(input("Enter your height in feet: "))
    if height_feet < 0:
      raise ValueError
    break
  except ValueError:
    print("Please enter your height in feet (no odd numbers): ")

while True:
  try:
    height_inches = int(input("Enter your height in inches: "))
    if not (0 <= height_inches <= 11):
      raise ValueError
    break
  except ValueError:
    print("Please enter your height in inches (0-11): ")

# Calculate BMI
bmi_result = calculate_bmi(weight_lbs, height_feet, height_inches)

# Interpret BMI
bmi_category = interpret_bmi(bmi_result)

# Out the results
print(f"\nYour BMI is: {bmi_result: .2f}")
print(f"You're in the {bmi_category} category.")
time.sleep(3)
print("Would you like any suggestions on how to improve your health?")
