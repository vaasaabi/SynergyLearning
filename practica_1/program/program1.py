import datetime
import locale

# 1. Запрос информации о дате рождения
day = int(input("Введите день рождения (ДД): "))
month = int(input("Введите месяц рождения (ММ): "))
year = int(input("Введите год рождения (ГГГГ): "))
birth_date = datetime.date(year, month, day)

# 2. Определение дня недели
def get_weekday(date):
    locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')
    return date.strftime("%A")

# 3. Проверка на високосный год
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 4. Определение возраста пользователя
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# 5. Форматирование даты
def format_date_with_stars(date):
    day_str = str(date.day).zfill(2)
    month_str = str(date.month).zfill(2)
    year_str = str(date.year)
    formatted_date = f"{day_str} {month_str} {year_str}"
    return ' '.join(char if char == ' ' else '*' for char in formatted_date)

# Вывод результатов
print(f"Ваш день рождения: {get_weekday(birth_date)}")
print(f"Високосный год: {'Да' if is_leap_year(year) else 'Нет'}")
print(f"Сейчас вам {calculate_age(birth_date)} лет")
print("Дата рождения в формате дд мм гггг:")
print(format_date_with_stars(birth_date))