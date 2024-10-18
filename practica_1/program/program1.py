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

# 5. Форматирование цифр в (*)
digits_patterns = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        " *** "
    ],
    '2': [
        " *** ",
        "*   *",
        "   * ",
        "  *  ",
        "*****"
    ],
    '3': [
        " *** ",
        "    *",
        "  ** ",
        "    *",
        " *** "
    ],
    '4': [
        "   * ",
        "  ** ",
        " * * ",
        "*****",
        "   * "
    ],
    '5': [
        "*****",
        "*    ",
        "**** ",
        "    *",
        "**** "
    ],
    '6': [
        " *** ",
        "*    ",
        "**** ",
        "*   *",
        " *** "
    ],
    '7': [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   "
    ],
    '8': [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** "
    ],
    '9': [
        " *** ",
        "*   *",
        " ****",
        "    *",
        " *** "
    ],
    ' ': [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]
}
def display_date_as_stars(date_string):
    lines = ["", "", "", "", ""]
    for ch in date_string:
        if ch in digits_patterns:
            pattern = digits_patterns[ch]
            for i in range(5):
                lines[i] += pattern[i] + "  "
        else:
            for i in range(5):
                lines[i] += "     "
    for line in lines:
        print(line)

# Вывод результатов
print(f"Ваш день рождения: {get_weekday(birth_date)}")
print(f"Високосный год: {'да' if is_leap_year(year) else 'нет'}")
print(f"Сейчас вам {calculate_age(birth_date)} лет")
date_str = f"{day:02} {month:02} {year}"
print("Ваша дата рождения:")
display_date_as_stars(date_str)