def exercises():
    exercise = input("Sequencial Structure\nSelection Structure\nRepetition Structure\nWhich type do you want to choose? ")
    # Sequencial
    if exercise.lower() == 'sequencial structure':
        exercise1_6 = input("Enter 1 to 6: ")
        if exercise1_6.lower() == '1':
            # Weighted average between 5 numbers
            num1, num2 = float(input("Number one? ")), float(input("Number two? "))
            num3, num4, num5 = float(input("Number three? ")), float(input("Number four? ")), float(input("Number five? "))
            weight1, weight2 = float(input("Weight number one?")), float(input("Weight number two?"))
            weight3, weight4, weight5 = float(input("Weight number three?")), float(input("Weight number four?")), float(input("Weight number five?"))
            # Calculation of the average
            result1 = (num1 * weight1) + (num2 * weight2) + (num3 * weight3) + (num4 * weight4) + (num5 * weight5)
            result2 = (weight1 + weight2) + (weight3 + weight4) + (weight5)
            Result = (result1 / result2)
            # Exit
            print(f"The weighted average = {Result}")

while True:
    exercises()
    restartcont = input("Do you want to open another application? (Yes/No): ")
    if restartcont.lower() != 'yes':
        break
