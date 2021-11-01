from sys import argv

salary, worked_hour, rate, benefit = argv

print("Имя скрипта: ", salary)
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Выработка в часах: ", worked_hour)
print("Ставка в час: ", rate)
print("Премия: ", benefit)
print("Зарплата сотрудника: ", (float(worked_hour) * float(rate)) + float(benefit))