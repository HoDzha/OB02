class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self._name = name  # Защищенный атрибут
        self._access_level = 'user'  # Уровень доступа обычного пользователя

    # Геттеры для доступа к атрибутам
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Сеттер для изменения имени
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            raise ValueError("Имя должно быть непустой строкой")

    # Метод для вывода информации о пользователе
    def display_info(self):
        return f"ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа администратора

    # Метод для добавления пользователя в список пользователей
    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")
        else:
            print("Ошибка: Невозможно добавить пользователя. Некорректный тип данных.")

    # Метод для удаления пользователя из списка пользователей по user_id
    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален из системы.")
                return
        print(f"Ошибка: Пользователь с ID {user_id} не найден.")


# Пример использования системы

# Создание админа
admin = Admin(1, "Ho Dzha")

# Список пользователей
user_list = []

# Добавление пользователей через администратора
user1 = User(2, "Amber")
user2 = User(3, "Baragozz")


user_list.append(admin)
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)

# Показ всех пользователей
for user in user_list:
    print(user.display_info())

# Удаление пользователя
admin.remove_user(user_list, 2)

# Показ всех пользователей после удаления
for user in user_list:
    print(user.display_info())
