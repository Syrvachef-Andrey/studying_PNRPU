import random


class User():
    def __init__(self, name_of_user, list_of_requests):
        self.user = name_of_user
        self.need_equipment = list_of_requests
        self.answers = {
            "1": "Заказано вычисление математического моделирования",
            "2": "Заявка на обучение нейронной сети",
            "3": "Рендеринг 3D-модели",
            "4": "Заявка на сверление малогабаритной детали",
            "5": "Заявка на сверление крупногабаритной детали",
            "6": "По вашей разводке создание малогабаритной электронной схемы",
            "7": "По вашей разводке создание крупногабаритной электронной схемы",
            "8": "Ваша 3D-модель будет напечатана полимерами",
            "9": "Ваша 3D-модель будет напечатана фотополимерами"
        }

    def main(self):
        print(f"Пользователь: {self.user}")
        for req in self.need_equipment:
            if str(req) in self.answers:
                print(self.answers[str(req)])


class Equipment:
    def __init__(self, name_of_user, list_of_requests):
        self.rand_names = ['Andrey', 'Yulia', 'Anna', 'Valerii']
        self.gpu = {"NVIDIA 4090": 24, "NVIDIA H200": 141, "NVIDIA A100": 80}
        self.drilling_machine = {"2K52": "Radial-drilling Machine", "2C132": "Vertical-drilling Machine"}
        self.electricity_scheme = {"Кумир-2": "Small scheme", "Контур-800ПП": "Big scheme"}
        self.printer_3D = {"Creality Ender 3S1 Pro": "Polymers", "Anycubic Photon Mono X": "Photopolymers"}

        self.queue = {
            "gpu": {random.choice(list(self.gpu.keys())): random.choice(self.rand_names)
                    for _ in range(random.randint(1, 4))},
            "drilling_machine": {random.choice(list(self.drilling_machine.keys())): random.choice(self.rand_names)
                                 for _ in range(random.randint(1, 4))},
            "electricity_scheme": {random.choice(list(self.electricity_scheme.keys())): random.choice(self.rand_names)
                                   for _ in range(random.randint(1, 4))},
            "printer_3D": {random.choice(list(self.printer_3D.keys())): random.choice(self.rand_names)
                           for _ in range(random.randint(1, 4))}
        }
        self.add_to_queue = list_of_requests
        self.user_name = name_of_user

    def main(self):
        for req in self.add_to_queue:
            if req == 1:  # Если запрос на GPU
                self.queue['gpu'].update({'NVIDIA 4090': self.user_name})
            elif req == 2:
                self.queue['gpu'].update({'NVIDIA H200': self.user_name})
            elif req == 3:
                self.queue['gpu'].update({'NVIDIA A100': self.user_name})
            elif req == 4:
                self.queue['drilling_machine'].update({'2K52': self.user_name})
            elif req == 5:
                self.queue['drilling_machine'].update({'2C132': self.user_name})
            elif req == 6:
                self.queue['electricity_scheme'].update({"Кумир-2": self.user_name})
            elif req == 7:
                self.queue['electricity_scheme'].update({'Контур-800ПП': self.user_name})
            elif req == 8:
                self.queue['printer_3D'].update({'Creality Ender 3S1 Pro': self.user_name})
            elif req == 9:
                self.queue['printer_3D'].update({'Anycubic Photon Mono X': self.user_name})

        print("Актуальная очередь:")
        for category, items in self.queue.items():
            print(f"\n{category}:")
            for item, name in items.items():
                print(f"  {item}: {name}")


# Ввод данных
print("Введите имя пользователя")
name_of_user = input()

print('\nСправка о подаче заявки на оборудования сервиса "CampusSE":')
print("Введите номер необходимого оборудования:")
print("1. Вычисление математического моделирования")
print("2. Обучение нейронных сетей")
print("3. Рендер 3д моделей")
print("4. Сверление малогабаритных деталей")
print("5. Сверление крупногабаритных деталей")
print("6. Создание малогабаритной электронной схемы по вашей разводке")
print("7. Создание крупногабаритной электронной схемы по вашей разводке")
print("8. Печать 3D детали полимерами по вашему .stl файлу")
print("9. Печать 3D детали фотополимерами по вашему .stl файлу")

list_of_requests = list(map(int, input("Введите номера через пробел: ").split()))

# Создание объектов
just_man = User(name_of_user, list_of_requests)
queue_of_man = Equipment(name_of_user, list_of_requests)

# Запуск
just_man.main()
queue_of_man.main()