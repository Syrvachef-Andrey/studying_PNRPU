import random

class User():
    def __init__(self):
        self.user = name_of_user
        self.need_equipment = list_of_requests
        self.answers = {"1": "Заказано вычисление математического моделирования",
                        "2": "Заявка на обучение нейронной сети",
                        "3": "Рендеринг 3D-модели",
                        "4": "Заявка на сверление малогабаритной детали",
                        "5": "Заявка на сверление крупногабаритной детали",
                        "6": "По вашей разводке создание малогабаритной электронной схемы",
                        "7": "По вашей разводке создание крупногабаритной электронной схемы",
                        "8": "Ваша 3D-модель будет напечатана полимерами",
                        "9": "Ваша 3D-модель будет напечатана фотополимерами"}

    def main(self):
        print(self.user)
        for i in self.need_equipment:
            if i == 1:
                print("")

class Equipment:
    def __init__(self):
        self.gpu = {"NVIDIA 4090": 24,
                    "NVIDIA H200": 141,
                    "NVIDIA A100": 80}
        self.drilling_machine = {"2K52": "Radial-drilling Machine",
                                 "2C132": "Vertical-drilling Machine"}
        self.electricity_scheme = {"Кумир-2": "Small scheme",
                                   "Контур-800ПП": "Big scheme"}
        self.printer_3D = {"Creality Ender 3S1 Pro": "Polymers",
                           "Anycubic Photon Mono X": "Photopolymers"}
        self.queue = {"gpu": [random.choice(list(self.gpu.keys())) for _ in range(random.randint(1, 5))],
                      "drilling_machine": [random.choice(list(self.drilling_machine.keys())) for _ in range(random.randint(1, 5))],
                      "electricity_scheme": [random.choice(list(self.electricity_scheme.keys())) for _ in range(random.randint(1, 5))],
                      "printer_3D": [random.choice(list(self.printer_3D.keys())) for _ in range(random.randint(1, 5))]
                      }
        self.add_to_queue = list_of_requests

    def main(self):

        print("Актуальная очередь: \n", self.queue)

print("Введите имя пользователя\n")
name_of_user = input()
list_of_requests = []
print('Справка о подаче заявки на оборудования сервиса "CampusSE":\n')
print("Введите номер необходимого оборудования:\n",
      "1. Вычисление математического моделирования\n",
      "2. Обучение нейронных сетей\n",
      "3. Рендер 3д моделей\n",
      "4. Сверление малогабаритных деталей\n",
      "5. Сверление крупногабаритных деталей\n",
      "6. Создание малогабаритной электронной схемы по вашей разводке\n",
      "7. Создание крупногабаритной электронной схемы по вашей разводке\n",
      "8. Печать 3D детали полимерами по вашему .stl файлу\n",
      "9. Печать 3D детали фотополимерами по вашему .stl файлу")
list_of_requests.append(int(input()))
print()
just_man = User()
man_with_equipment = Equipment()


just_man.main()
man_with_equipment.main()
