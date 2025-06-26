i = 0
for marks in (36, 96, -10, 67, 75, 40, 21):
    i += 1
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