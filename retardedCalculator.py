toContinue = True
while toContinue:
    print("Welcome to the Retarded Calculator.\nEnter a expression to solve it.")
    userInput = input()
    if "+" in userInput:
        additionInput = userInput.split("+")
        print(float(additionInput[0]) + float(additionInput[1]))
    if "-" in userInput:
        subtractionInput = userInput.split("-")
        print(float(subtractionInput[0]) - float(subtractionInput[1]))
    if "*" in userInput:
        multiplicationInput = userInput.split("*")
        print(float(multiplicationInput[0]) * float(multiplicationInput[1]))
    if "/" in userInput:
        divisionInput = userInput.split("/")
        print(float(divisionInput[0]) / float(divisionInput[1]))