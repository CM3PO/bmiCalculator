# BMI Calculator

A simple Python-based Body Mass Index (BMI) calculator that helps users determine their BMI category and provides optional health suggestions.

## Features

- **BMI Calculation**: Calculates BMI using weight in pounds and height in feet/inches
- **Input Validation**: Ensures all user inputs are valid and within expected ranges
- **BMI Categories**: Classifies results as Underweight, Normal, Overweight, or Obese
- **Health Suggestions**: Optional tips for fitness, nutrition, or custom health requests
- **User-Friendly Interface**: Clear prompts and error handling for a smooth experience

## How to Use

1. Run the program
2. Enter your weight in pounds
3. Enter your height in feet and inches (0-11)
4. Enter your gender (Male, Female, or Prefer not to answer)
5. View your BMI result and category
6. Optionally receive health suggestions

## BMI Categories

- **Underweight**: BMI < 18.5
- **Normal**: BMI 18.5 - 24.9
- **Overweight**: BMI 25 - 29.9
- **Obese**: BMI ≥ 30

## Requirements

- Python 3.11 or higher

## Running the Application

Click the "Run" button in Replit or execute:

```bash
python main.py
```

## Example Output

```
Enter your weight in pounds: 150
Enter your height in feet: 5
Enter your height in inches (0–11): 8
Enter your gender (Male, Female, or Prefer not to answer): Male

Gender: Male
Your BMI is: 22.78
You are in the Normal category.

Would you like any suggestions on how to improve your health?
Enter 'Y' or 'N': Y

What would you like help with?
Enter 'F' for Fitness, 'N' for Nutrition, or 'O' for Other.
Your choice: F

Fitness Tip: Aim for at least 30 minutes of moderate physical activity most days. Start with walking, stretching, or light strength training.
```

## Health Disclaimer

This BMI calculator is for informational purposes only and should not replace professional medical advice. Consult with a healthcare provider for personalized health guidance.
