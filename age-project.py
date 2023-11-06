def age_group(age):
  if age<18:
    return "Minor"
  elif age>=18 and age <=30:
    return "Adult"
  elif age>30:
    return "Senior"
  else:
    return "Invalid"
age=int(input("Enter your age: "))
age_group=age_group(age)
print(f"You are {age_group}")  