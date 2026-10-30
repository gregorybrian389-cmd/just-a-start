#SECTION A
#I.	Write a Python statement that reads an exam score from the user, converts it to an integer, and stores it in a variable called score.
#II.	Write an if-elif-else block that assigns a letter grade based on the score:  90–100 = 'A'  |  80–89 = 'B'  |  70–79 = 'C'  |  60–69 = 'D'  |  below 60 = 'F' Also print: 'Pass' if grade is A, B, or C, otherwise print 'Fail'.
#answer
score = int(input("Enter your exam score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)
if grade in ['A', 'B', 'C']:
    print("Pass")
else:
    print("Fail")




#SECTION B
#I.	Write a complete Python program that repeatedly asks a user to enter a valid percentage mark (an integer between 0 and 100 inclusive). The program must: reject any value outside 0–100 with the message 'Invalid mark. Enter a value between 0 and 100.' accept a valid value and print 'Mark recorded: X' use a while loop for validate.
while True:
    mark = int(input("Enter a percentage mark (0–100): "))
    
    if 0 <= mark <= 100:
        print("Mark recorded:", mark)
        break
    else:
        print("Invalid mark. Enter a value between 0 and 100.")



#GROUP WORK (GROUP 1 MEMBER)
#I.	Write a Python function called calculate bmi that takes two parameters: weight kg (float) and height_m (float). The function must: calculate BMI using the formula: BMI = weight / (height²) return the BMI rounded to 2 decimal places include a correct docstring use a meaningful variable name for the result before returning it
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
bmi = round(bmi, 2)
print("Your BMI is:", bmi)




#II.	Write two lines of code that call calculate bmi with weight=70 and height=1.75, store the result in a variable, and print it with an f-string showing 2 decimal places.
#Write a complete Python program that manages student grades. The program must:
#•	Define a function get_grade(score) that accepts an integer score (0–100) and returns the corresponding letter grade (A/B/C/D/F) based on standard boundaries (A≥90, B≥80, C≥70, D≥60, F<60).
#•	Define a function collect_scores(n) that uses a loop to collect n valid integer scores from the user (validate each score is between 0 and 100) and returns them as a list.
#•	Define a function generate_report(scores) that calculates and returns a dictionary containing: the highest score, the lowest score, the mean (average), and a count of how many students passed (score ≥ 50).
#•	In the main program: ask how many students there are, collect their scores using your function, generate the report, and display all results with clear formatting using f-strings.
#•	Add a docstring to each function.


