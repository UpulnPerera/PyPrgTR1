i = 0
try:
    for marks in range(1, 6):
        marks = int(input("Please enter the marks: "))
        while marks < 0 or marks > 100:
            i += 1
            print("Invalid input")
            marks = int(input("Please enter the marks: "))


        if marks < 0 or marks > 100:
            print(f"Student {i} marks is invalid")
        elif marks >= 75:
            print(f"Student {i} have obtained A")
        elif marks >= 60:                                               
            print(f"Student {i} have obtained B")                                                                                                                           
        elif marks >= 50:
            print(f"Student {i} have obtained C")
        elif marks >= 35:
            print(f"Student {i} have obtained C")
        else:
            print(f"Student {i} have obtained W")

except ValueError:
    print(f"Invalid input. Please enter a valid figure.") 