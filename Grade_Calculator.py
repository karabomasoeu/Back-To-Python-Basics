def grade_calculator():
  
   score = int(input("Enter your the percentage of your mark: ").replace("%", ""))
  
    if score >= 90:
        print(f"Your grade is an A")
    elif score >= 80:
        print(f"Your grade is a B")
    elif score >= 70:
        print(f"Your grade is a C")
    elif score >= 60:
        print(f"Your grade is a D")
    else:
        print(f"Your grade is an F")
      
grade_calculator()
