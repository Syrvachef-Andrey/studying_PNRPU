import random
import tkinter as tk
from tkinter import messagebox, ttk


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
        for category in self.categories.values():
            num_requests = random.randint(1, 5)
            for _ in range(num_requests):
                option_id = random.choice(list(category["options"].keys()))
                user = random.choice(self.user_names)
                category["queue"].append((option_id, user))

    def add_user_requests(self, user_name, requests):
        for req in requests:
            for category in self.categories.values():
                if req in category["options"]:
                    category["queue"].append((req, user_name))
                    break


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CampusSE Equipment Service")
        self.geometry("800x600")

        self.system = EquipmentSystem()
        self.system.generate_random_requests()
        self.current_user = None

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_window()

        tk.Label(self, text="Введите имя пользователя:", font=("Arial", 14)).pack(pady=10)

        self.name_entry = tk.Entry(self, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Button(self, text="Продолжить", command=self.show_info, font=("Arial", 12)).pack(pady=20)

    def show_info(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Ошибка", "Пожалуйста, введите имя пользователя")
            return

        self.current_user = User(name, [])
        self.clear_window()

        info_text = """
        Прежде чем начать работу в нашем сервисе обязательна к прочтению справка по работе оборудования:

        3D-печать:
        Классические полимеры подходят для прочных и крупных деталей, а фотополимерные смолы – для высокодетализированных и мелких объектов с гладкой поверхностью.

        Обучение моделей нейронных сетей и вычисления физ. или мат. моделирования:
        GPU ускоряют нейросети, научные расчёты и рендеринг 3D-моделей благодаря массовому параллелизму.

        Для работы с сверлильными станками:
        Детали с задачами на сверление отверстий более 25мм считаются крупногабаритными, менее - малогабаритными

        Для работы с станками для электронных плат:
        Схема с количеством элементов на плате более 100 - крупногабартиная, менее - малогабаритная
        """

        text_widget = tk.Text(self, wrap=tk.WORD, font=("Arial", 11))
        text_widget.insert(tk.END, info_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        tk.Button(self, text="Я ознакомился с информацией", command=self.show_request_form,
                  font=("Arial", 12)).pack(pady=20)

    def show_request_form(self):
        self.clear_window()

        tk.Label(self, text="Справка о подаче заявки на оборудования сервиса CampusSE:",
                 font=("Arial", 14)).pack(pady=10)

        options_text = """
        Введите номера необходимого оборудования (через пробел):
        1. Вычисление математического моделирования (NVIDIA 4090)
        2. Обучение нейронных сетей (NVIDIA H200)
        3. Рендер 3D моделей (NVIDIA A100)
        4. Сверление малогабаритных деталей (2K52)
        5. Сверление крупногабаритных деталей (2C132)
        6. Создание малогабаритной электронной схемы (Кумир-2)
        7. Создание крупногабаритной электронной схемы (Контур-800ПП)
        8. Печать 3D детали полимерами (Creality Ender 3S1 Pro)
        9. Печать 3D детали фотополимерами (Anycubic Photon Mono X)
        """

        text_widget = tk.Text(self, wrap=tk.WORD, font=("Arial", 11), height=12)
        text_widget.insert(tk.END, options_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(pady=10, padx=10)

        tk.Label(self, text="Введите номера через пробел:", font=("Arial", 12)).pack(pady=5)

        self.request_entry = tk.Entry(self, font=("Arial", 12))
        self.request_entry.pack(pady=5)

        tk.Button(self, text="Отправить заявки", command=self.process_requests,
                  font=("Arial", 12)).pack(pady=20)

    def process_requests(self):
        try:
            requests = list(map(int, self.request_entry.get().split()))
            valid_requests = [r for r in requests if 1 <= r <= 9]

            if not valid_requests:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные номера (1-9)")
                return

            self.current_user.requests = valid_requests
            self.system.add_user_requests(self.current_user.name, valid_requests)
            self.show_results()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, вводите только числа через пробел")

    def show_results(self):
        self.clear_window()

        # Показываем заявки пользователя
        tk.Label(self, text=f"Пользователь: {self.current_user.name}",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self, text="Подтвержденные заявки:", font=("Arial", 12)).pack()

        for req in self.current_user.requests:
            text = self.current_user.responses.get(req, "")
            tk.Label(self, text=f"- {text}", font=("Arial", 11), anchor="w").pack(fill=tk.X)

        # Показываем очереди
        tk.Label(self, text="\nТекущее состояние очередей:",
                 font=("Arial", 14, "bold")).pack(pady=20)

        notebook = ttk.Notebook(self)

        for cat_name, category in self.system.categories.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=cat_name.upper())

            if not category["queue"]:
                tk.Label(frame, text="Очередь пуста", font=("Arial", 11)).pack(pady=10)
                continue

            for i, (option_id, user) in enumerate(category["queue"], 1):
                equipment = category["options"][option_id]
                text = f"{i}. {equipment} — {user}"
                if user == self.current_user.name:
                    tk.Label(frame, text=text, font=("Arial", 11, "bold"),
                             fg="green").pack(anchor="w")
                else:
                    tk.Label(frame, text=text, font=("Arial", 11)).pack(anchor="w")

        notebook.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        tk.Button(self, text="Завершить", command=self.destroy,
                  font=("Arial", 12)).pack(pady=20)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = Application()
    app.mainloop()