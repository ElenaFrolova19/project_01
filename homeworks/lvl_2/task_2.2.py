# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

# Решение

month = input("Введите номер месяца: ")
def quarter_of(month):
    if month.isdigit():
        month = int(month)
        if month >= 1 and month <= 3:
            months = ["январь", "февраль", "март"]
            month_name = months[month - 1]
            return(f'месяц {month} ({month_name}) является частью первого квартала')
        elif  month >= 4 and month <= 6:
            months = ["апрель", "май", "июнь"]
            month_name = months[month - 4]
            return(f'месяц {month} ({month_name}) является частью второго квартала')
        elif month >= 7 and month <= 9:
            months = ["июль", "август", "сентябрь"]
            month_name = months[month - 7]
            return(f'месяц {month} ({month_name}) является частью третьего квартала')  
        elif month >= 10 and month <= 12:
            months = ["октябрь", "ноябрь", "декабрь"]
            month_name = months[month - 10]
            return(f'месяц {month} ({month_name}) является частью четвертого квартала')         
        else:
            return "Ошибка ввода данных"
    else:
        return "Ошибка ввода данных"
print(quarter_of(month))
