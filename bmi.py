def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        
        print(f"Your BMI is {bmi:.2f}. Category: {category}")
    except ValueError:
        print("Invalid input! Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()
