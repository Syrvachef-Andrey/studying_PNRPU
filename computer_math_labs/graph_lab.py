import numpy as np
import random as rnd

from torch.distributed.rpc import new_method

while 1:
    print("Введите размерность матрицы от 2 до 10: ", end='')
    n = int(input())
    if n < 2 or n > 10:
        print("Вы ввели неправльную размерность, попробуйте снова")
    else:
        print("Размерность матрицы:", n)
        break

my_matrix = np.zeros((n, n), int)

for i in range(len(my_matrix)):
    for j in range(len(my_matrix[i])):
        if i == j:
            my_matrix[i][j] = 1
        else:
            my_matrix[i][j] = rnd.randint(0, 1)
print(my_matrix)

new_matrix = my_matrix

for i in range(n):
    new_matrix = np.dot(new_matrix, my_matrix)

print(new_matrix)

transp_matrix = np.transpose(my_matrix)

conquat_matrix = transp_matrix * my_matrix

print(my_matrix, end="\n\n")
print(transp_matrix, end="\n\n")
print(conquat_matrix)
#
# import socket
# import logging
#
#
# class SocketListener:
#     def __init__(self, config):
#         self.printer = config.get_printer()
#         self.reactor = self.printer.get_reactor()
#
#         # Чтение IP и PORT из конфигурации
#         self.ip = '192.168.1.194'  # Устанавливаем значение по умолчанию
#         self.port = 5000  # Устанавливаем значение по умолчанию
#
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Повторное использование адреса
#         try:
#             self.server_socket.bind((self.ip, self.port))
#         except socket.error as e:
#             raise RuntimeError(f"Failed to bind to {self.ip}:{self.port}: {e}")
#
#         self.gcode = self.printer.lookup_object('gcode')
#         self.gcode.register_command('LIDAR_READ_DATA', self.read_data_raw)
#
#         self.server_socket.listen(5)
#         self.client_socket = None
#         self.client_address = None
#         self.received_data = None  # Атрибут для хранения данных
#         self.printer.register_event_handler("klippy:connect", self.handle_connect)
#         self.printer.register_event_handler("klippy:disconnect", self.handle_disconnect)
#
#     def handle_connect(self):
#         self.reactor.register_timer(self.accept_connection, self.reactor.NOW)
#
#     def handle_disconnect(self):
#         if self.client_socket:
#             self.client_socket.close()
#         if self.server_socket:
#             self.server_socket.close()
#
#     def accept_connection(self, eventtime):
#         try:
#             # Пробуем принять соединение
#             self.client_socket, self.client_address = self.server_socket.accept()
#             self.client_socket.setblocking(False)  # Устанавливаем неблокирующий режим
#             logging.info(f"Connected by {self.client_address}")
#
#             # Запускаем таймер для постоянного чтения данных
#             self.reactor.register_timer(self.read_data, self.reactor.NOW)
#         except socket.error as e:
#             # Если произошла ошибка при принятии соединения
#             logging.error(f"Failed to accept connection: {e}")
#             # Проверяем, есть ли подключение к OPI
#             if not self.is_opi_connected():
#                 logging.warning("OPI is not connected. Stopping the module.")
#                 self.stop_module()
#             else:
#                 # Если OPI подключен, повторяем попытку принять соединение
#                 self.accept_connection()
#
#     def read_data_raw(self, gcmd):
#         if self.received_data:
#             gcmd.respond_raw(f"Data from lidar: {self.received_data}")
#         else:
#             gcmd.respond_raw("No data received yet.")
#
#     def is_opi_connected(self):
#         # Логика проверки подключения к OPI
#         # Например, можно проверить, доступен ли IP и порт OPI
#         try:
#             # Пробуем установить соединение с OPI
#             test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             test_socket.settimeout(1)  # Устанавливаем таймаут для проверки
#             test_socket.connect((self.ip, self.port))
#             test_socket.close()
#             return True  # Если соединение установлено
#         except (socket.error, socket.timeout):
#             return False  # Если соединение не установлено
#
#     def stop_module(self):
#         # Логика остановки модуля
#         logging.info("Stopping the module due to lack of OPI connection.")
#         if self.client_socket:
#             self.client_socket.close()
#         self.server_socket.close()
#         self.printer.request_exit('opi_disconnected')  # Запрос на выход из Klipper
#
#     def read_data(self, eventtime):
#         if not self.client_socket:
#             logging.warning("No client socket available, retrying connection.")
#             self.reactor.register_callback(self.accept_connection)
#             return self.reactor.NEVER
#
#         try:
#             # Проверяем, есть ли данные в сокете
#             data = self.client_socket.recv(1024)
#             if data == b'':  # Проверяем, если данные пустые (соединение закрыто)
#                 logging.info("No data received, restarting socket")
#                 self.client_socket.close()
#                 self.client_socket = None
#                 self.reactor.register_callback(self.accept_connection)  # Принимаем новое соединение
#                 return self.reactor.NEVER  # Останавливаем таймер, чтобы не продолжать чтение
#             if data != b'':
#                 # Обработка полученных данных
#                 self.received_data = data.decode('utf-8')  # Сохранение данных
#                 logging.info(f"Received data: {self.received_data}")
#             else:
#                 # Если данные не пришли, просто продолжаем опрос
#                 pass
#         except BlockingIOError:
#             # Если данных нет, продолжаем опрос
#             pass
#         except socket.error as e:
#             logging.error(f"Socket error: {e}")
#             self.client_socket.close()
#             self.client_socket = None
#             return self.reactor.NEVER
#         # Регистрируем таймер для повторного вызова read_data через 1 секунды
#         return eventtime + 1
#
#     def get_status(self, eventtime):
#         if self.received_data:
#             try:
#                 return {'received_data': float(self.received_data)}
#             except ValueError:
#                 return {'received_data': self.received_data}
#         return {'received_data': 0.0}
#
#
# def load_config(config):
#     return SocketListener(config)
