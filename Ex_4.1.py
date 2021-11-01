from sys import argv

salary, worked_hour, rate, benefit = argv

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Your pay is equal {calculation}")