# Create a dictionary named student scores where keys are student names values are scores (integers)
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 70 # Added an extra a student for more data
}

print("---Initial Student Scores---")
# Iterate through the dictionary
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")

# Add a new student and their score to the dictionary.
new_student_name = "Grace"
new_student_score = 90
student_scores[new_student_name] = new_student_score
print(f"---Added New Student: {new_student_name} with score {new_student_score}" )
for name, score in student_scores.items():
    print(f"{name}: {score}")

# Find the student with the highest score and print their names and score
if student_scores: # Ensure the dictionary is not empty
    highest_score = 0
    highest_scorer_name = ""
    for name, score in student_scores.items():
        if score > highest_score:
            highest_score = score
            highest_scorer_name = name
    print(F"--- Student with the highest score ---")
    print(f"{highest_scorer_name}: {highest_score}\n")
else:
    print("The dictionary is empty, cannot find the highest score.\n")    

# Create a new dictionary containing only student
high_achievers = {}
for name, score in student_scores.items():
    if score >= 90:
        high_achievers[name] = score

print("---High achievers (Score 90 or above ) ---")
if high_achievers:
    for name, score in high_achievers.items():
        print(f"{name} : {score}")
else:
    print("No students scored 90 or above")



    