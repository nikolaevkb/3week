users = {"Иван": "3916",
         "Катя": "1298",
         "Лена": "0010"}
def phonebook(name, users, default="undefined"):
    if name in users:
        return users[name]
    return default

print(phonebook("Иван", users))

# Дополнительное задание.
# Выберите наилучший вариант:
# №3 "Словарь-справочник это глобальный объект (переменная), которая передается в функцию как параметр."