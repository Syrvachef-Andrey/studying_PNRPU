import random


class User:
    def __init__(self, name, requests):
        self.name = name
        self.requests = requests
        self.responses = {
            1: "Заказано вычисление математического моделирования",
            2: "Заявка на обучение нейронной сети",
            3: "Рендеринг 3D-модели",
            4: "Заявка на сверление малогабаритной детали",
            5: "Заявка на сверление крупногабаритной детали",
            6: "По вашей разводке создание малогабаритной электронной схемы",
            7: "По вашей разводке создание крупногабаритной электронной схемы",
            8: "Ваша 3D-модель будет напечатана полимерами",
            9: "Ваша 3D-модель будет напечатана фотополимерами"
        }

    def show_requests(self):
        print(f"\nПользователь: {self.name}")
        print("Подтвержденные заявки:")
        for req in self.requests:
            if req in self.responses:
                print(f"- {self.responses[req]}")


class EquipmentSystem:
    def __init__(self):
        self.categories = {
            "gpu": {
                "options": {
                    1: "NVIDIA 4090 (24GB)",
                    2: "NVIDIA H200 (141GB)",
                    3: "NVIDIA A100 (80GB)"
                },
                "queue": []
            },
            "drilling": {
                "options": {
                    4: "2K52 (Radial-drilling Machine)",
                    5: "2C132 (Vertical-drilling Machine)"
                },
                "queue": []
            },
            "electronics": {
                "options": {
                    6: "Кумир-2 (Small scheme)",
                    7: "Контур-800ПП (Big scheme)"
                },
                "queue": []
            },
            "printing": {
                "options": {
                    8: "Creality Ender 3S1 Pro (Polymers)",
                    9: "Anycubic Photon Mono X (Photopolymers)"
                },
                "queue": []
            }
        }
        self.user_names = ['Andrey', 'Yulia', 'Anna', 'Valerii']

    def generate_random_requests(self):
        """Генерирует случайные запросы для имитации работы системы"""
        for category in self.categories.values():
            num_requests = random.randint(1, 5)
            for _ in range(num_requests):
                option_id = random.choice(list(category["options"].keys()))
                user = random.choice(self.user_names)
                category["queue"].append((option_id, user))

    def add_user_requests(self, user_name, requests):
        """Добавляет запросы пользователя в систему"""
        for req in requests:
            for category in self.categories.values():
                if req in category["options"]:
                    category["queue"].append((req, user_name))
                    break

    def show_queue(self):
        """Выводит текущее состояние очередей"""
        print("\nТекущее состояние очередей:")
        for cat_name, category in self.categories.items():
            print(f"\n{cat_name.upper()}:")
            if not category["queue"]:
                print("  Очередь пуста")
                continue

            for i, (option_id, user) in enumerate(category["queue"], 1):
                equipment = category["options"][option_id]
                print(f"  {i}. {equipment} — {user}")


def main():
    print("Введите имя пользователя:")
    user_name = input().strip()

    print('\nСправка о подаче заявки на оборудования сервиса "CampusSE":')
    print("Введите номер необходимого оборудования:")
    print("1. Вычисление математического моделирования (NVIDIA 4090)")
    print("2. Обучение нейронных сетей (NVIDIA H200)")
    print("3. Рендер 3D моделей (NVIDIA A100)")
    print("4. Сверление малогабаритных деталей (2K52)")
    print("5. Сверление крупногабаритных деталей (2C132)")
    print("6. Создание малогабаритной электронной схемы (Кумир-2)")
    print("7. Создание крупногабаритной электронной схемы (Контур-800ПП)")
    print("8. Печать 3D детали полимерами (Creality Ender 3S1 Pro)")
    print("9. Печать 3D детали фотополимерами (Anycubic Photon Mono X)")

    requests = list(map(int, input("Введите номера через пробел: ").split()))

    # Создаем систему и пользователя
    system = EquipmentSystem()
    system.generate_random_requests()  # Заполняем случайными запросами
    system.add_user_requests(user_name, requests)

    user = User(user_name, requests)

    # Выводим результаты
    user.show_requests()
    system.show_queue()


if __name__ == "__main__":
    main()