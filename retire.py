from datetime import datetime

current_year = datetime.now().year

age = input('What is your age? ')
retire = input('At what age would you like to retire? ')
years = int(retire) - int(age)

print(f"It's 2024. You will retire in {current_year + years}.")
print(f"You have only {years} years of work to go!")